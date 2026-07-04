# Data Quality Issue Register Template

Use this register to summarize defects in a reviewer-friendly format.

| Issue ID | DQ Dimension | Field / Area | Business Rule | Scope | Defect Definition | Evidence File | Count | Impact | Severity | Recommendation | Validation Needed | Status |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| DQ-001 | Completeness | diagnosis_code | Diagnosis code should be populated when required | Appointment records | diagnosis_code is missing | flagged_critical_nulls_20260512.csv | TBD | Reporting completeness risk | Medium | Confirm rule and review missing values | Confirm when diagnosis code is required | Draft |
| DQ-002 | Validity | age_years | Age should be within realistic range | Appointment records | age is negative, 150, or 999 | flagged_impossible_values_20260512.csv | 16 | Validity and demographic reporting risk | High | Review source values and correction rules | Confirm valid age limits | Draft |
| DQ-003 | Uniqueness | appointment identifier | Repeated IDs require review | Appointment records | Same ID appears more than once | notebook evidence | TBD | Duplicate or relationship interpretation risk | Medium | Investigate whether repeated IDs represent duplicates or valid repeated activity | Confirm grain of the dataset | Draft |

## Severity Guide

| Severity | Meaning |
|---|---|
| Critical | Issue may affect high-trust reporting, financial reporting, audit review, or major operational decisions. |
| High | Issue affects important operational reporting or downstream workflows. |
| Medium | Issue affects analysis quality but has limited immediate operational risk. |
| Low | Issue is mostly cosmetic, minor, or low-volume. |

## Review Notes

Severity should be based on:

- affected record count
- affected percentage
- downstream dependency
- business impact
- whether the defect can be corrected
- whether the defect can be prevented at source

## Status Values

| Status | Meaning |
|---|---|
| Draft | Rule or impact still needs validation |
| Confirmed | Rule and defect definition were confirmed |
| In Review | Data owner or business owner is reviewing |
| Fixed | Correction was applied and tested |
| Monitored | Ongoing check or alert exists |
