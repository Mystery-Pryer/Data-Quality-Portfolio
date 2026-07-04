# Pandas EDA and Wrangling Summary

## Purpose

This note summarizes the professional version of the exploratory pandas work for the healthcare appointment project. The goal is to describe what was inspected, what quality risks were observed, and what cleaning or validation steps should follow.

## Dataset Profile

Initial pandas inspection loaded a synthetic appointment dataset with:

```text
Rows: 650
Columns: 15
```

Main fields inspected included appointment identifiers, name fields, gender, age, nationality, department, visit type, appointment date/time, payment type, consultation cost, doctor name, follow-up flag, waiting time, and diagnosis code.

## Observed Data Quality Themes

| Area | Example issue type | Why it matters |
|---|---|---|
| Missing values | Missing department, visit type, appointment time, or diagnosis code | Can weaken reporting and operational analysis |
| Standardization | Mixed casing and variants in gender, nationality, department, visit type, payment type, and follow-up values | Can split categories and make grouped reporting unreliable |
| Date and time parsing | Multiple date formats and time formats | Can affect scheduling, trend analysis, and timeliness checks |
| Numeric cleaning | Cost and waiting-time values may appear as numbers or text with units/currency labels | Can break calculations and KPI reporting |
| Naming consistency | Doctor names may include inconsistent casing or prefixes | Can affect grouping and attribution analysis |
| Validity | Unexpected values such as unknown, maybe, or non-standard categories | Requires business confirmation before mapping |

## Professional Wrangling Plan

1. Preserve a raw copy before cleaning.
2. Standardize column names into snake_case.
3. Normalize blank-like values to null.
4. Trim leading/trailing spaces in text columns.
5. Standardize known categorical variants only when the mapping is defensible.
6. Parse dates and times into consistent formats.
7. Extract numeric values from cost and waiting-time fields.
8. Keep raw and cleaned versions of important fields where auditability matters.
9. Produce a data quality issue register with counts, impact, and recommended validation.

## Important Rule

Do not silently fix ambiguous values. If a value has unclear business meaning, flag it for review instead of forcing it into a category.

Examples:

- Confirm whether `Unknown` is an accepted value or a defect.
- Confirm whether `Maybe` is allowed for follow-up status.
- Confirm whether all visit type variants can be safely mapped to approved categories.

## Portfolio Framing

This EDA work demonstrates pandas-based data profiling, early defect discovery, cleaning design, and the habit of separating raw evidence from cleaned reporting fields.
