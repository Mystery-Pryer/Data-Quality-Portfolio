# Healthcare Appointment Data Quality Investigation

## Project Summary

This project investigates synthetic healthcare appointment data using a Data Quality Engineering workflow. The goal is to identify missing, invalid, inconsistent, duplicated, or relationship-breaking records and translate the evidence into business risks and recommendations.

Core case format:

```text
Business rule -> Scope -> Defect definition -> Evidence -> Interpretation -> Business risk -> Validation needed
```

## Current Status

Portfolio project in progress. Current work includes business-rule documentation, pandas EDA summary, completeness check planning, and stakeholder-ready findings structure.

## Business Context

Appointment data can support billing readiness, eligibility checks, provider reporting, audit trails, operations, performance metrics, and downstream reconciliation. Data quality issues can weaken trust in those outputs.

## Initial Data Quality Dimensions

| Dimension | Example question |
|---|---|
| Completeness | Are required fields populated? |
| Standardization / Conformity | Do values follow approved formats and categories? |
| Integrity | Do records link to valid reference data? |
| Validity | Are values inside realistic ranges or accepted domains? |
| Uniqueness | Are duplicate records inflating counts? |
| Timeliness | Are dates aligned with status and workflow timing? |

## Current Check Plan

The first check pack focuses on completeness:

1. Missing insurance code.
2. Completed appointments missing provider attribution.
3. Completed appointments missing appointment date.

These checks are draft rules until confirmed by a business owner or data owner.

## Repository Files

```text
sql/
  README.md

docs/
  business_rules.md
  pandas_eda_summary.md
  findings_template.md
  workflow.md
  dq_issue_register_template.md

data_sample/
  README.md

results/
  README.md
```

## Skills Demonstrated

- Data quality investigation mindset.
- SQL Server validation planning.
- Python/pandas data profiling and wrangling.
- Completeness and null/blank detection.
- Scope versus defect separation.
- Defect counts and defect percentages.
- Business-rule documentation.
- Stakeholder-ready findings structure.
- Connecting technical data issues to operational and reporting risk.

## Next Steps

- Add sample synthetic data extract.
- Add reviewed SQL completeness checks.
- Add pandas profiling notebook or script.
- Add standardization checks for status, visit type, department, and insurance values.
- Add integrity checks against reference tables.
- Add duplicate and near-duplicate detection.
- Add a completed findings summary with sample outputs.
