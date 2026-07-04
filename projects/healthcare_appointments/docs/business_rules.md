# Healthcare Appointment Data Quality Rules

All rules in this document are draft rules until confirmed by a business owner or data owner.

## Rule Groups

This project currently contains two layers of rules:

1. **Active pandas cleaning rules** used in the appointment wrangling output.
2. **Planned SQL validation rules** for deeper completeness, integrity, and relationship checks.

## Active Pandas Cleaning Rules

### Column names

**Draft rule:** Source column names should be converted to stable snake_case names before cleaning values.

**Why it matters:** Stable field names make cleaning code repeatable and reduce breakage when source exports have spacing or punctuation differences.

**Validation:**

- Strip leading/trailing spaces.
- Convert to lowercase.
- Replace spaces with underscores.
- Remove non-alphanumeric characters except underscores.

### gender

**Draft rule:** Gender values should map to an approved controlled list or remain null when unknown.

**Why it matters:** Mixed abbreviations and unknown values can split grouped reporting.

**Validation:**

- Map known values such as `M`, `Male`, `MALE` to `male`.
- Map known values such as `F`, `Female`, `FEM` to `female`.
- Flag null, unknown, or unmapped values for review.

### department

**Draft rule:** Department values should map to approved department names.

**Why it matters:** Department variants can make facility or service-line reporting unreliable.

**Validation:**

- Map known variants such as `PEDS` to `pediatrics`.
- Map known variants such as `DERM` to `dermatology`.
- Map known variants such as `GP` to `general`.
- Flag missing or unmapped values.

### visit_type

**Draft rule:** Visit type values should map to approved categories.

**Why it matters:** Inconsistent visit labels can distort appointment volume and workflow analysis.

**Validation:**

- Map known follow-up variants to `follow_up`.
- Map emergency, consultation, and procedure variants to approved values.
- Flag missing or unmapped values.

### payment_type

**Draft rule:** Payment type should map to approved categories.

**Why it matters:** Payment category quality affects revenue grouping, waiver analysis, and operational reporting.

**Validation:**

- Map insurance variants to `insurance`.
- Map self-pay variants to `self_pay`.
- Map corporate variants to `corporate`.
- Preserve free/waived categories where they are valid.
- Flag missing or unmapped values.

### follow_up_required

**Draft rule:** Follow-up status should use approved values.

**Why it matters:** Ambiguous follow-up values can affect care coordination and operational follow-up reporting.

**Validation:**

- Map clear yes/no variants.
- Keep ambiguous values such as `maybe` visible for review unless the business confirms the meaning.
- Flag missing or unresolved values.

### nationality

**Draft rule:** Nationality values should map to approved reporting categories.

**Why it matters:** Inconsistent values can split demographic reporting.

**Validation:**

- Map known variants such as `UAE` to `emirati` when confirmed.
- Keep unknown or missing values flagged.

### appointment_date and appointment_time

**Draft rule:** Appointment date and time should parse into consistent date and time fields.

**Why it matters:** Date/time quality affects scheduling analysis, trend reporting, and timeliness checks.

**Validation:**

- Parse supported date formats.
- Flag invalid or missing dates.
- Parse supported time formats.
- Flag invalid or missing times.

### age_years

**Draft rule:** Age should be populated and within a realistic range.

**Why it matters:** Impossible ages indicate source-entry or transformation defects and may distort analysis.

**Validation:**

- Flag missing ages.
- Flag impossible values such as negative ages, 150, or 999.

### consultation_cost and waiting_time_mins

**Draft rule:** Cost and waiting time should be numeric after cleaning.

**Why it matters:** Text, currency labels, or unit labels can break calculations and KPI reporting.

**Validation:**

- Extract numeric values where the mapping is clear.
- Convert free/complimentary values to zero only when the business rule supports it.
- Flag missing or unresolved values.

### diagnosis_code

**Draft rule:** Diagnosis code should be populated when required by the workflow.

**Why it matters:** Missing diagnosis codes can affect reporting completeness and downstream review.

**Validation:**

- Flag missing values.
- Confirm when a diagnosis code is required.

## Planned SQL Validation Rules

### provider attribution

**Draft rule:** Completed appointments should have valid provider attribution where required.

**Validation:**

- Filter to completed appointments.
- Count missing or invalid provider fields.
- Review whether attribution can exist in another field.

### reference integrity

**Draft rule:** Operational codes should match approved reference lists where reference tables exist.

**Validation:**

- Check department, facility, provider, or category codes against reference tables.
- Flag orphan values that do not match the reference list.

### duplicate identifier review

**Draft rule:** Repeated identifiers should be reviewed before treating them as duplicate records.

**Validation:**

- Identify repeated IDs.
- Compare key fields across repeated records.
- Confirm whether the repeated ID represents duplicate entry, repeat activity, or valid relationship behavior.
