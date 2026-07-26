from __future__ import annotations

import csv
import json
import py_compile
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
TEXT_EXTENSIONS = {
    ".csv",
    ".json",
    ".md",
    ".py",
    ".sql",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
FORBIDDEN_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    ".env.development",
}
FORBIDDEN_SUFFIXES = {".db", ".sqlite", ".sqlite3"}
MAX_TEXT_BYTES = 10 * 1024 * 1024


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def validate_csv(path: Path, problems: list[str]) -> dict[str, int]:
    rows = 0
    columns = 0
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle)
            header = next(reader, None)
            if header is None:
                problems.append(f"{path.relative_to(ROOT)}: empty CSV")
                return {"rows": 0, "columns": 0}
            columns = len(header)
            if columns == 0 or not any(cell.strip() for cell in header):
                problems.append(f"{path.relative_to(ROOT)}: missing CSV header")
            duplicate_headers = sorted({name for name in header if name and header.count(name) > 1})
            if duplicate_headers:
                problems.append(
                    f"{path.relative_to(ROOT)}: duplicate CSV headers {duplicate_headers}"
                )
            for line_number, row in enumerate(reader, start=2):
                rows += 1
                if len(row) != columns:
                    problems.append(
                        f"{path.relative_to(ROOT)}:{line_number}: expected {columns} columns, found {len(row)}"
                    )
    except (UnicodeDecodeError, csv.Error) as exc:
        problems.append(f"{path.relative_to(ROOT)}: CSV parse error ({exc})")
    return {"rows": rows, "columns": columns}


def main() -> int:
    problems: list[str] = []
    files = tracked_files()
    python_files = 0
    csv_files = 0
    markdown_files = 0
    csv_rows = 0

    if not (ROOT / "README.md").is_file():
        problems.append("Missing root README.md")

    for path in files:
        relative = path.relative_to(ROOT)
        if path.name in FORBIDDEN_NAMES:
            problems.append(f"{relative}: environment file must not be committed")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            problems.append(f"{relative}: local database file must not be committed")
        if not path.is_file():
            continue

        suffix = path.suffix.lower()
        if suffix not in TEXT_EXTENSIONS:
            continue
        if path.stat().st_size > MAX_TEXT_BYTES:
            problems.append(f"{relative}: text file exceeds 10 MB validation limit")
            continue

        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            problems.append(f"{relative}: text file is not valid UTF-8")
            continue

        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.startswith("<<<<<<< ") or line.startswith(">>>>>>> "):
                problems.append(
                    f"{relative}:{line_number}: unresolved merge-conflict boundary"
                )

        if suffix == ".py":
            python_files += 1
            try:
                py_compile.compile(str(path), doraise=True)
            except py_compile.PyCompileError as exc:
                problems.append(f"{relative}: Python syntax error ({exc.msg})")
        elif suffix == ".csv":
            csv_files += 1
            stats = validate_csv(path, problems)
            csv_rows += stats["rows"]
        elif suffix == ".md":
            markdown_files += 1

    ARTIFACTS.mkdir(exist_ok=True)
    summary = {
        "repository": ROOT.name,
        "tracked_files": len(files),
        "python_files_compiled": python_files,
        "csv_files_validated": csv_files,
        "csv_data_rows_checked": csv_rows,
        "markdown_files_checked": markdown_files,
        "status": "pass" if not problems else "fail",
        "problems": problems,
    }
    (ARTIFACTS / "repository-quality-summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    if problems:
        print("Repository validation failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(
        f"Validated {len(files)} tracked files, compiled {python_files} Python files, "
        f"checked {csv_files} CSV files and {markdown_files} Markdown files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
