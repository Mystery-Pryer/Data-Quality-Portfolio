# SQL Checks

This folder is reserved for SQL Server validation checks for the appointment data quality project.

The pandas pipeline currently produces cleaned data and review outputs. SQL checks will be added to validate the cleaned outputs and reproduce key DQ findings using database logic.

## Planned SQL Check Groups

| Check group | Purpose |
|---|---|
| Completeness | Count missing required fields by business scope |
| Standardization | Validate category values against approved lists |
| Validity | Detect unrealistic values such as impossible ages |
| Uniqueness | Review repeated identifiers and possible duplicates |
| Integrity | Check relationships against reference tables when available |
| Timeliness | Validate date/time logic after parsing |

## SQL Pattern

Use this pattern when building checks:

```text
WHERE = business scope
CASE = defect logic
COUNT = population size
SUM(CASE) = defect count
GROUP BY = where the issue appears
HAVING = show affected groups
```

## Next SQL Files

Recommended next files:

```text
01_completeness_checks.sql
02_standardization_checks.sql
03_validity_checks.sql
04_duplicate_identifier_checks.sql
05_reference_integrity_checks.sql
```
