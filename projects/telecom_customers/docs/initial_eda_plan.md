# Telecom Customer Initial EDA Plan

## Purpose

This note defines a professional starting point for the telecom customer data quality project.

## Initial Dataset Profile

The early exploratory notebook loaded a synthetic telecom customer dataset with:

```text
Rows: 750
Columns: 13
```

The notebook is not copied into this portfolio yet because it is still an early work file. The portfolio version should be cleaned before publishing.

## Planned Data Quality Focus

| Area | Example check |
|---|---|
| Completeness | Required customer and account fields are populated |
| Standardization | Phone, email, status, plan, and region values follow agreed formats |
| Duplicate detection | Possible duplicate customer records are identified |
| Validity | Values follow accepted ranges, formats, or domains |
| Consistency | Account status, plan, and activity fields do not contradict each other |
| Integrity | Customer, account, plan, and usage records link correctly |

## Planned Workflow

1. Load synthetic telecom customer data into pandas.
2. Preserve raw data before cleaning.
3. Profile columns, nulls, distinct values, duplicates, and data types.
4. Build business rules for customer identity, contact details, account status, and plan fields.
5. Translate rules into SQL and pandas checks.
6. Summarize issues in a DQ issue register.
7. Document findings with evidence, risk, recommendation, and validation needed.

## Portfolio Rule

Only cleaned, reviewed, and reproducible work should be copied into this repo. Early notebooks with local paths, error outputs, or scratch cells should stay in the private learning workspace until polished.
