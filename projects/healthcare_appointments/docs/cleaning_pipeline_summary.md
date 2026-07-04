# Healthcare Appointment Cleaning Pipeline Summary

## Purpose

This document summarizes the completed healthcare appointment wrangling work from the private Data Quality lab in a portfolio-safe format.

The original work was exploratory and notebook-based. This summary converts it into a professional data quality case study: what was messy, how it was cleaned, what was flagged, and why the work matters.

## Source Dataset

The synthetic raw appointment dataset contained 650 rows and 15 source columns.

The raw file included intentionally messy operational healthcare data such as:

- Inconsistent column names with spaces and punctuation.
- Mixed gender values such as full words, abbreviations, unknown values, and blanks.
- Mixed department and visit-type labels.
- Multiple date and time formats.
- Payment values stored as inconsistent categories.
- Consultation cost values stored as text, numbers, currency strings, or free/complimentary labels.
- Waiting-time values stored as numbers or text with units.
- Missing diagnosis codes and other required fields.
- Duplicate patient identifiers that require review.

## Cleaning and Profiling Work Completed

### 1. Column standardization

Source columns were cleaned into consistent snake_case field names.

Example source-to-cleaned structure:

| Raw field style | Clean field style |
|---|---|
| Patient ID | patient_id |
| Patient  Name | patient_name |
| Age (years) | age_years |
| Appointment  Time | appointment_time |
| Follow Up Required? | follow_up_required |
| Waiting Time (mins) | waiting_time_mins |
| Diagnosis Code | diagnosis_code |

### 2. Categorical standardization

Several fields were mapped from messy raw values into controlled categories.

| Field | Cleaned examples |
|---|---|
| gender | male, female, null when unknown/invalid |
| department | pediatrics, general, dermatology, cardiology, orthopedics |
| visit_type | follow_up, emergency, consultation, procedure |
| payment_type | insurance, self_pay, corporate, free, waived |
| follow_up_required | yes, no, maybe/null depending on business rule |
| nationality | emirati, indian, pakistani, british, filipino, other |

### 3. Date, time, and numeric cleaning

The notebook work included cleaning logic for appointment dates, appointment times, consultation costs, and waiting-time values.

Important examples:

- Multiple appointment date formats were parsed into a consistent date field.
- Multiple time formats were parsed into a consistent time field.
- Consultation cost was normalized from mixed text/numeric/currency values into numeric output.
- Waiting time was normalized from strings such as values with minute labels into numeric minutes.

### 4. Flag columns added

The cleaned output kept original analytical fields and added data quality flag columns.

Important flag columns included:

- flag_gender
- flag_department
- flag_visit_type
- flag_payment_type
- flag_follow_up_required
- flag_nationality
- flag_diagnosis_code_missing
- flag_appointment_date_invalid
- flag_appointment_date_missing
- flag_appointment_time_invalid
- flag_appointment_time_missing
- flag_age_years_missing
- flag_age_years_impossible
- flag_consultation_cost_missing
- flag_waiting_time_mins_missing

## Output Files from Private Lab

The private lab produced these useful outputs:

| Output | Portfolio meaning |
|---|---|
| dha_appointments_clean_20260512.csv | Cleaned appointment dataset with normalized fields and DQ flags |
| flagged_critical_nulls_20260512.csv | Records requiring review due to critical missing fields |
| flagged_impossible_values_20260512.csv | Records with impossible values such as unrealistic ages |

## Key Quality Findings

### 1. Standardization issues

The raw dataset included many category variants for gender, department, visit type, payment type, follow-up flag, and nationality. These issues can split categories and make grouped reporting unreliable.

### 2. Missing critical values

The flagged critical-null output shows records with missing or unresolved values across key fields such as gender, department, visit type, payment type, follow-up status, nationality, diagnosis code, appointment date, age, cost, or waiting time.

### 3. Impossible age values

The impossible-values output identified age values such as -1, 150, and 999. These should be treated as defects or source-system entry issues unless a business owner confirms a special coding rule.

### 4. Duplicate patient identifiers

The notebook work identified duplicate patient IDs. These may represent true duplicates, repeat visits using the same patient key, or key-quality problems. The correct interpretation requires business validation.

## Professional Notes

This work is stronger than a simple EDA because it includes both cleaning and quality-control thinking:

- Raw data was preserved before transformation.
- Values were standardized into controlled vocabularies.
- Ambiguous values were flagged instead of silently forced into categories.
- Quality flags were added to preserve auditability.
- Outputs were separated into clean data and review queues.

## Recommended Next Portfolio Step

Convert the notebook into a clean Python script:

```text
scripts/clean_healthcare_appointments.py
```

The script should read a sample raw CSV, apply the cleaning rules, generate the clean output, and export flagged records for review.
