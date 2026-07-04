# Data Quality Workflow

Use this workflow for each data quality case in the appointment project.

## Core Model

```text
Process -> Meaning -> Rule -> Check -> Evidence -> Impact -> Prevention
```

## Case Structure

1. **Business process** — What operational workflow created or uses the data?
2. **Business meaning** — Why does the field, table, or relationship matter?
3. **Business rule** — What should be true if the data is usable?
4. **Scope / population** — Which rows are included before measuring the issue?
5. **Defect definition** — What exact condition makes a row fail the rule?
6. **Check logic** — Which pandas or SQL logic proves the issue?
7. **Evidence** — Count, percentage, sample records, output file, or screenshot.
8. **Interpretation** — What does the result mean?
9. **Impact** — What report, workflow, or decision may become unreliable?
10. **Validation needed** — What assumption must be confirmed?
11. **Recommendation** — Clean, flag, monitor, fix at source, or ask for rule confirmation.

## Current Project Workflow

The appointment project currently follows this flow:

```text
raw appointment data
-> pandas profiling
-> column standardization
-> category mapping
-> date/time and numeric cleaning
-> DQ flag generation
-> cleaned output
-> flagged review outputs
-> business-rule documentation
-> future SQL validation checks
```

## SQL Principle

Use `WHERE` for business scope and `CASE` expressions for defect counting.

Example mental model:

```text
WHERE = population
CASE = defect logic
COUNT = population size
SUM(CASE) = defect count
GROUP BY = where the issue appears
HAVING = show affected groups
```

## Pandas Principle

Do not hide defects during cleaning. Keep audit-friendly flags so a reviewer can see what changed and which records still need attention.

Examples:

- Cleaned values should be analysis-ready.
- Flag columns should preserve evidence of unresolved or suspicious records.
- Review outputs should isolate rows that need rule confirmation or correction.
