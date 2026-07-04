# Data Quality Portfolio

Portfolio of data quality investigation projects using SQL, Python/pandas, data profiling, business-rule validation, issue registers, and stakeholder-ready findings.

This repository shows how messy operational data can be converted into trusted analysis assets: profile the data, define rules, clean values, flag defects, document evidence, explain impact, and recommend next actions.

## Portfolio Focus

- Data quality investigation
- Python/pandas data wrangling
- SQL-based validation checks
- Business-rule documentation
- Data profiling and issue registers
- Root-cause thinking and evidence-based recommendations
- Separation of raw data, cleaned data, and review outputs

## Investigation Approach

The core investigation model used across the projects is:

```text
Process -> Meaning -> Rule -> Check -> Evidence -> Impact -> Prevention
```

In practical terms:

1. Understand the business process.
2. Identify what the data is supposed to prove.
3. Define the business rule.
4. Translate the rule into SQL or pandas checks.
5. Measure the issue and keep evidence.
6. Explain the impact.
7. Recommend validation, correction, monitoring, or prevention.

## Projects

| Project | Status | Focus | Tools |
|---|---|---|---|
| [Healthcare Appointment Data Quality Investigation](projects/healthcare_appointments/README.md) | Active / in progress | pandas cleaning pipeline, cleaned output, flagged review outputs, DQ rules, SQL check planning | Python/pandas, SQL Server, DBeaver |
| [Telecom Customer Data Quality Investigation](projects/telecom_customers/README.md) | Planned | customer profile checks, contact standardization, duplicate detection, relationship checks | SQL, Python/pandas |

## Repository Structure

```text
projects/
  healthcare_appointments/
    README.md
    data_sample/
      dha_appointments_clean_20260512.csv
    results/
      flagged_critical_nulls_20260512.csv
      flagged_impossible_values_20260512.csv
    docs/
    sql/
  telecom_customers/
    README.md
    docs/
```

## What This Portfolio Demonstrates

This portfolio demonstrates the habits of a junior Data Quality Engineer / Data Quality Analyst:

- Turning vague data problems into testable business rules.
- Using pandas and SQL to validate assumptions.
- Preserving evidence while creating cleaned, analysis-ready outputs.
- Separating business scope from defect logic.
- Creating flag columns and review outputs instead of hiding defects.
- Connecting technical defects to operational and reporting risk.
- Documenting findings clearly enough for business or data owners to review.

## Data Note

All datasets in this portfolio are synthetic or sample data.

## Status

This repository is still being polished. The healthcare appointment project is the strongest current portfolio project; the telecom project is a planned next case study.
