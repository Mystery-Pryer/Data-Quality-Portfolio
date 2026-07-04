# Healthcare Appointment Data Quality Findings Summary

## Purpose

This document summarizes the current findings from the healthcare appointment data quality project. It uses the cleaned dataset and flagged review outputs as evidence.

## Evidence Files

| Evidence file | What it shows |
|---|---|
| `data_sample/dha_appointments_clean_20260512.csv` | Cleaned appointment data with normalized values and DQ flag columns |
| `results/flagged_critical_nulls_20260512.csv` | Records with important missing or unresolved fields |
| `results/flagged_impossible_values_20260512.csv` | Records with impossible age values |

## Finding 1: Category Standardization Was Required

### Dimension

Standardization / conformity

### Evidence

The cleaned output includes normalized fields for gender, nationality, department, visit type, payment type, and follow-up status. The original work required mapping many raw variants into controlled values.

### Interpretation

The raw appointment data was not ready for reliable grouped reporting without standardization. If left uncleaned, the same business concept could appear as multiple categories.

### Impact

Reporting by gender, department, visit type, payment type, or follow-up status could be split across inconsistent labels.

### Recommendation

Keep controlled mapping rules documented and validate them with a business or data owner before treating them as final.

## Finding 2: Critical Missing or Unresolved Values Exist

### Dimension

Completeness

### Evidence

The project contains a flagged review output for critical missing or unresolved values:

```text
results/flagged_critical_nulls_20260512.csv
```

### Interpretation

Some records still require review after cleaning because important fields were missing, blank, unknown, or unresolved.

### Impact

Missing values can affect operational analysis, appointment reporting, diagnosis completeness, and review workflows.

### Recommendation

Review the flagged output by field and decide whether each issue should be corrected, backfilled, excluded from reporting, or monitored.

## Finding 3: Impossible Age Values Were Identified

### Dimension

Validity

### Evidence

The project contains an impossible-values review output:

```text
results/flagged_impossible_values_20260512.csv
```

The file contains records with unrealistic age values such as negative ages, 150, and 999.

### Interpretation

These values are unlikely to represent valid patient ages unless the source system uses special placeholder codes.

### Impact

Impossible ages can distort demographic analysis and may indicate source-entry, extraction, or transformation issues.

### Recommendation

Confirm valid age rules with the data owner. Until confirmed, keep these records flagged rather than silently correcting them.

## Finding 4: Repeated Identifiers Require Review

### Dimension

Uniqueness / grain definition

### Evidence

The notebook work identified repeated appointment-related identifiers.

### Interpretation

Repeated identifiers should not automatically be treated as duplicates. They may represent duplicate entries, repeat activity, or a dataset-grain misunderstanding.

### Impact

Incorrect duplicate handling can either inflate counts or wrongly remove valid activity records.

### Recommendation

Confirm the grain of the dataset before removing repeated identifiers. Define whether one row represents a patient, appointment, visit, or appointment event.

## Overall Recommendation

The current healthcare project should be treated as a strong pandas-based data quality case study. The next improvement is to convert the notebook logic into a clean Python script and add SQL checks that reproduce the key findings from the cleaned outputs.
