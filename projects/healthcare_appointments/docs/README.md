# Healthcare Appointment Documentation

This folder contains the documentation layer for the healthcare appointment data quality project.

## Documentation Map

| Document | Purpose |
|---|---|
| `cleaning_pipeline_summary.md` | Explains the pandas cleaning pipeline, output files, flag columns, and main quality themes |
| `pandas_eda_summary.md` | Summarizes the EDA and wrangling work from the appointment dataset |
| `business_rules.md` | Defines draft data quality rules for cleaned fields and planned SQL checks |
| `findings_summary.md` | Summarizes current findings from the cleaned and flagged outputs |
| `dq_issue_register_template.md` | Provides a reusable register format for DQ issues |
| `findings_template.md` | Provides a reusable structure for stakeholder-ready findings |
| `workflow.md` | Explains the investigation workflow used across the project |

## Project Logic

```text
raw appointment data
-> pandas profiling
-> cleaning and standardization
-> DQ flag generation
-> cleaned output
-> review outputs
-> findings and recommendations
-> SQL validation planning
```

## Current Evidence Files

```text
data_sample/dha_appointments_clean_20260512.csv
results/flagged_critical_nulls_20260512.csv
results/flagged_impossible_values_20260512.csv
```
