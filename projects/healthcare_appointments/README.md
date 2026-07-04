# Healthcare Appointment Data Quality Investigation

## Project Summary

This project investigates a synthetic appointment dataset using a Data Quality Engineering workflow. The goal is to profile messy data, clean important fields, flag records that need review, and translate defects into evidence-based findings.

Core case format:

```text
Business rule -> Scope -> Defect definition -> Evidence -> Interpretation -> Impact -> Validation needed
```

## Current Status

Active portfolio project. The project now includes a cleaned appointment output, flagged review outputs, business-rule documentation, pandas EDA notes, a cleaning pipeline summary, and SQL check planning.

## Business Context

Appointment data can support scheduling, eligibility review, provider attribution, operations reporting, audit trails, performance metrics, and downstream reconciliation. Data quality issues can weaken trust in those outputs.

## Work Completed So Far

- Profiled a synthetic appointment dataset with 650 rows and 15 source columns.
- Standardized messy column names into snake_case fields.
- Normalized category fields such as gender, department, visit type, payment type, follow-up status, and nationality.
- Cleaned date, time, cost, and waiting-time fields into more analysis-ready formats.
- Added quality flag columns to identify records needing review.
- Produced a cleaned appointment output and flagged review outputs.
- Documented the cleaning pipeline, quality findings, business rules, and reusable finding templates.

## Data Quality Dimensions Covered

| Dimension | Current evidence |
|---|---|
| Completeness | Critical-null review output and missing-value flags |
| Standardization / Conformity | Controlled mappings for category fields |
| Validity | Impossible-value output for unrealistic ages |
| Uniqueness | Duplicate identifier review noted from notebook work |
| Timeliness | Date and time parsing logic prepared for future checks |
| Integrity | SQL relationship checks planned as a next step |

## Key Files

```text
data_sample/
  dha_appointments_clean_20260512.csv

results/
  flagged_critical_nulls_20260512.csv
  flagged_impossible_values_20260512.csv

docs/
  cleaning_pipeline_summary.md
  pandas_eda_summary.md
  business_rules.md
  dq_issue_register_template.md
  findings_template.md
  workflow.md

sql/
  README.md
```

## Skills Demonstrated

- Python/pandas data profiling and wrangling.
- Column standardization.
- Controlled-value mapping.
- Date/time and numeric-field cleaning.
- Data quality flag generation.
- Completeness and null/blank detection.
- Impossible-value detection.
- Duplicate-key review.
- SQL validation planning.
- Business-rule documentation.
- Stakeholder-ready findings structure.

## Next Steps

- Convert notebook cleaning logic into a clean Python script.
- Add SQL completeness checks.
- Add standardization checks for key category fields.
- Add integrity checks against reference tables.
- Add duplicate and near-duplicate detection.
- Add a completed findings summary using the current review outputs.
