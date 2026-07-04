# Healthcare Appointment Data Quality Investigation

## Project Summary

This project investigates synthetic healthcare appointment data using a Data Quality Engineering workflow. The goal is to identify missing, invalid, inconsistent, duplicated, or relationship-breaking records and translate the evidence into business risks and recommendations.

The project is focused on investigation quality, not only technical checks. Each issue should connect:

```text
Business rule -> Scope -> Defect definition -> Evidence -> Interpretation -> Business risk -> Validation needed
```

## Current Status

Portfolio project in progress. The current version focuses on completeness checks and business-rule documentation. Additional dimensions such as validity, standardization, integrity, uniqueness, and timeliness will be added as the project matures.

## Data Privacy

The healthcare data is synthetic. It does not contain real patient data.

## Business Context

Appointment data may support billing readiness, eligibility checks, provider reporting, audit trails, clinical operations, facility-level performance metrics, and downstream reconciliation. Data quality issues can weaken trust in those outputs.

## Initial Data Quality Dimensions

| Dimension | Example question |
|---|---|
| Completeness | Are required fields populated? |
| Standardization / Conformity | Do values follow approved formats and categories? |
| Integrity | Do appointment records link to valid reference data? |
| Validity | Are values inside realistic ranges or accepted domains? |
| Uniqueness | Are duplicate records inflating counts? |
| Timeliness | Are dates logically aligned with status and workflow timing? |

## Current Checks

The current SQL check pack focuses on completeness:

1. Missing `insurance_code`.
2. Completed appointments missing `physician_id`.
3. Completed appointments missing `appointment_date`.

These checks are written as draft rules until confirmed by a business owner or data owner.

## Repository Files

```text
sql/
  01_completeness_checks.sql

docs/
  business_rules.md
  findings_template.md
  investigation_framework.md
  dq_issue_register_template.md

data_sample/
  README.md

outputs/
  README.md
```

## Skills Demonstrated

- SQL Server validation checks.
- Data profiling mindset.
- Completeness and null/blank detection.
- Scope versus defect separation.
- Defect counts and defect percentages.
- Business-rule documentation.
- Stakeholder-ready findings structure.
- Connecting technical data issues to operational and reporting risk.

## Next Steps

- Add sample synthetic data extract.
- Add pandas profiling notebook or script.
- Add standardization checks for appointment status, visit type, department, and insurance values.
- Add integrity checks against facility and physician reference tables.
- Add duplicate and near-duplicate detection.
- Add a completed findings summary with sample outputs.
