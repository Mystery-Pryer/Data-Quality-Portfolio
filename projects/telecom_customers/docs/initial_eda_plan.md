# Telecom Customer Initial EDA Plan

## Purpose

This note defines the starting point for the telecom customer data quality project.

The project will reuse the same investigation model:

```text
Business process -> Business rule -> Check -> Evidence -> Impact -> Recommendation
```

## Initial Dataset Profile

The early exploratory notebook loaded a synthetic telecom customer dataset with:

```text
Rows: 750
Columns: 13
```

The notebook is not copied into this portfolio yet because it is still an early work file.

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
4. Build business rules for identity, contact details, account status, and plan fields.
5. Translate rules into SQL and pandas checks.
6. Export cleaned data and flagged review outputs.
7. Summarize issues in a DQ issue register.
8. Document findings with evidence, impact, recommendation, and validation needed.

## Candidate Rules

| Area | Draft rule |
|---|---|
| Customer identity | Each record should have a stable customer ID |
| Contact details | Phone and email values should follow accepted formats where required |
| Account status | Status should use approved values only |
| Plan | Plan names or codes should match an approved list |
| Usage records | Usage records should link to a valid key |

## Portfolio Rule

Only cleaned, reviewed, and reproducible work should be copied into this repo.
