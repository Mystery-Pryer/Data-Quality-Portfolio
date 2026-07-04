# Pandas EDA and Wrangling Summary

## Purpose

This note summarizes the pandas exploration and wrangling work for the appointment data quality project. The focus is not only on cleaning values, but on identifying quality risks, preserving evidence, and creating review outputs.

## Dataset Profile

Initial pandas inspection loaded a synthetic appointment dataset with:

```text
Rows: 650
Columns: 15
```

Main fields inspected:

- appointment identifier
- name fields
- gender
- age
- nationality
- department
- visit type
- appointment date and time
- payment type
- consultation cost
- provider name
- follow-up flag
- waiting time
- diagnosis code

## Observed Data Quality Themes

| Area | Example issue type | Why it matters |
|---|---|---|
| Missing values | Missing department, visit type, time, diagnosis code, age, cost, or waiting time | Can weaken reporting and operational analysis |
| Standardization | Mixed casing and variants in gender, nationality, department, visit type, payment type, and follow-up values | Can split categories and make grouped reporting unreliable |
| Date and time parsing | Multiple date and time formats | Can affect scheduling, trend analysis, and timeliness checks |
| Numeric cleaning | Cost and waiting-time values stored as numbers, text, labels, or currency strings | Can break calculations and KPI reporting |
| Naming consistency | Provider names with prefixes, mixed casing, and spacing variations | Can affect grouping and attribution analysis |
| Validity | Unrealistic ages and ambiguous values | Requires validation before mapping or excluding |
| Uniqueness | Repeated identifiers | Requires review to separate true duplicates from repeated activity |

## Work Completed

1. Preserved a raw copy before transformation.
2. Standardized source column names into snake_case.
3. Normalized blank-like values to null.
4. Trimmed and standardized text columns.
5. Mapped known category variants into controlled values.
6. Parsed dates and times into consistent output fields.
7. Cleaned cost and waiting-time fields into numeric-friendly values.
8. Added quality flag columns for defects and unresolved values.
9. Exported a clean dataset and flagged review outputs.

## Review Outputs

| Output | Purpose |
|---|---|
| `dha_appointments_clean_20260512.csv` | Cleaned appointment dataset with normalized fields and DQ flags |
| `flagged_critical_nulls_20260512.csv` | Records requiring review due to missing critical fields |
| `flagged_impossible_values_20260512.csv` | Records requiring review due to impossible age values |

## Important Rule

Do not silently fix ambiguous values. If a value has unclear business meaning, flag it for review instead of forcing it into a category.

Examples:

- Confirm whether `Unknown` is an accepted value or a defect.
- Confirm whether `Maybe` is allowed for follow-up status.
- Confirm whether all visit type variants can be safely mapped to approved categories.
- Confirm whether repeated IDs represent duplicates, repeat visits, or valid relationship behavior.

## Portfolio Framing

This work demonstrates pandas-based data profiling, cleaning design, controlled mapping, flag generation, review-output creation, and separation of raw evidence from cleaned reporting fields.
