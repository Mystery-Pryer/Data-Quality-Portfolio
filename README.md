# Data Quality Portfolio

Portfolio of data quality investigation projects using SQL, Python/pandas, data profiling, business-rule validation, and stakeholder-ready findings.

This repository is designed to show how data quality work moves from messy data to trusted reporting: define the business rule, test the data, document evidence, explain business risk, and recommend next actions.

## Portfolio Focus

- Data quality investigation
- SQL-based validation checks
- Python/pandas data wrangling
- Business-rule documentation
- Data profiling and issue registers
- Root-cause thinking and evidence-based recommendations

## Investigation Approach

The core investigation model used across the projects is:

```text
Process -> Meaning -> Rule -> Check -> Impact -> Prevention
```

In practical terms:

1. Understand the business process.
2. Identify what the data is supposed to prove.
3. Define the business rule.
4. Translate the rule into SQL or pandas checks.
5. Measure the issue and document evidence.
6. Explain the business risk.
7. Recommend validation, correction, monitoring, or prevention.

## Projects

| Project | Status | Focus | Tools |
|---|---|---|---|
| [Healthcare Appointment Data Quality Investigation](projects/healthcare_appointments/README.md) | In progress | Completeness, standardization, integrity, validity, stakeholder-ready findings | SQL Server, DBeaver, Python/pandas |
| [Telecom Customer Data Quality Investigation](projects/telecom_customers/README.md) | Planned | Customer data profiling, standardization, duplicate detection, relationship checks | SQL, Python/pandas |

## Repository Structure

```text
projects/
  healthcare_appointments/
    README.md
    sql/
    docs/
    data_sample/
    results/
  telecom_customers/
    README.md
```

## What This Portfolio Demonstrates

This portfolio is intended to demonstrate the habits of a junior Data Quality Engineer / Data Quality Analyst:

- Turning vague data problems into testable business rules.
- Using SQL and pandas to validate assumptions.
- Separating business scope from defect logic.
- Calculating defect counts and defect percentages.
- Connecting technical defects to downstream reporting, billing, operations, audit, or decision risk.
- Documenting findings clearly enough for business or data owners to review.

## Data Privacy Note

All datasets in this portfolio are synthetic or sample data. No real patient, customer, or company-confidential data should be committed.

## Status

This repository is currently private while the healthcare project is being polished. It should be made public only when the project folders are clean, reproducible, and free of study-only notes or local artifacts.
