# Repository Continuity Rules

## Purpose

This public portfolio must remain accurate, reproducible, safe to publish, and understandable from any authorized machine. GitHub is the durable source of truth. Chat history, local notebooks, uncommitted outputs, browser state, and one machine's database are temporary execution context only.

## Source-of-truth order

1. Verified remote repository state.
2. Committed project documentation, business rules, scripts, SQL, issue registers, findings, and approved outputs.
3. Verified source evidence referenced by repository records.
4. Current user instruction.
5. Chat or machine-local context only when it does not conflict with the repository.

When sources conflict, stop and document the discrepancy rather than silently choosing one.

## Session start

Before substantive work:

1. Confirm the repository, `origin`, branch, and target project.
2. Run `git fetch --prune` and inspect `git status -sb`.
3. Compare local and remote history; fast-forward only when the working tree is clean and the branch is only behind.
4. Stop on dirty, divergent, unexpected-remote, conflict, or unresolved-ahead states.
5. Re-read the portfolio README, the selected project README, business rules, workflow, findings, and relevant validator.
6. Record the governing remote commit SHA in substantive run evidence or handoffs.

Never use force push, hard reset, automatic rebase, automatic merge, or automatic stash/pop to conceal synchronization problems.

## Portfolio evidence standard

Every published project must make it possible to determine:

- the business context and project scope;
- whether the data is synthetic, sample, restricted, or public;
- which rules are confirmed and which remain draft assumptions;
- which scripts, notebooks, SQL, and outputs produced the evidence;
- what defects were measured and how;
- what cleaning or standardization changed;
- what evidence was preserved for review;
- what business or reporting risk was identified;
- what validation, limitation, or next step remains;
- the durable commit containing the published result.

A portfolio summary must not replace required source code, rule documentation, review outputs, findings, or reproducibility instructions.

## Accuracy and publication safety

- Publish only synthetic, sample, sanitized, or explicitly approved material.
- Never publish credentials, personal data, real patient/customer records, private business rules, local database files, or restricted artifacts.
- Keep raw/source samples, cleaned outputs, and flagged review outputs clearly separated.
- Preserve provenance and audit-friendly evidence.
- Do not hide defects during cleaning.
- Do not label draft rules as confirmed business rules.
- Do not claim production deployment, business impact, machine-learning capability, or validation that the repository does not prove.
- Keep README claims consistent with the actual files and current project status.
- Record uncertainty and blockers explicitly instead of converting them into confident facts.

## Canonical locations

Use each project's existing structure and keep one canonical location for every artifact. Avoid parallel folders with overlapping purpose. Uncertain but useful material should remain in an explicitly labelled staging, review, or archive location until it is suitable for publication.

Repository-specific validation remains in `scripts/`, while shared generic quality checks are called from `Mystery-Pryer/repo-automation` using a pinned version.

## Session end

A meaningful session is complete only when:

1. applicable repository and project validators have run;
2. README claims, status, findings, and outputs are internally consistent;
3. limitations, assumptions, blockers, and next steps are documented;
4. only scoped and publication-safe files are committed;
5. the branch is pushed;
6. the remote is fetched again;
7. the intended commit and paths are confirmed remotely;
8. the issue or pull request is updated when applicable.

Do not claim publication readiness or completion when required evidence is missing, validators fail, or remote verification was not performed.

## Clean-machine test

Periodically clone the repository into an empty directory and verify that an external reviewer can understand and reproduce the selected project using only committed instructions and public-safe assets. Record missing dependencies, hidden manual steps, broken links, absent outputs, stale claims, and undocumented assumptions as portfolio defects.
