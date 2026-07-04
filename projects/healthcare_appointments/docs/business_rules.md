# Healthcare Appointment Data Quality Rules

All rules in this document are draft rules until confirmed by a business owner or data owner.

## Completeness

### insurance_code

**Draft rule:** `insurance_code` should be populated for appointment records where insurance information is required.

**Why it matters:** Missing insurance codes can affect billing readiness, eligibility checks, payer reporting, claims preparation, and downstream reconciliation.

**Draft validation:**

- Flag records where `insurance_code` is null.
- Flag records where `insurance_code` is blank after trimming spaces.
- Review whether the rule applies to all appointments or only insured, billable, completed, or non-cancelled appointments.

## Standardization and Integrity

### facility_code

**Draft rule:** `facility_code` should follow the approved facility code format and exist in the facility reference table.

**Why it matters:** Invalid facility codes can break facility-level reporting and joins to reference data.

**Draft validation:**

- Flag null or blank facility codes.
- Flag facility codes not found in the facility registry.
- Flag facility codes with leading or trailing spaces.

## Integrity

### physician_id

**Draft rule:** Completed appointments should have a valid `physician_id` where provider attribution is required.

**Why it matters:** Missing or invalid physician IDs can affect provider reporting, audit trails, clinical operations, billing attribution, and performance metrics.

**Draft validation:**

- Flag completed appointments with missing physician IDs.
- Flag physician IDs not found in the physician registry.
- Confirm whether non-physician staff can complete visits and whether provider attribution is stored elsewhere.

## Validity and Timeliness

### appointment_date

**Draft rule:** Completed appointments should have a valid `appointment_date`.

**Why it matters:** Missing or invalid dates can affect scheduling, billing timing, wait-time reporting, audit trails, and operational metrics.

**Draft validation:**

- Flag completed appointments with missing appointment dates.
- Flag appointment dates that cannot be parsed as valid dates if stored as text.
- Flag scheduled appointments in the past if the business rule says they should have been updated.

## Validity

### age

**Draft rule:** `age` should be within a realistic human range for healthcare appointment records.

**Why it matters:** Impossible ages indicate source entry issues or transformation defects and may distort demographic reporting.

**Draft validation:**

- Flag negative ages.
- Flag ages equal to zero if not valid for the population being analyzed.
- Flag ages above the agreed maximum threshold.

## Conformity

### department

**Draft rule:** Department values should follow the approved department code or department name standard.

**Why it matters:** Inconsistent department values weaken reporting and make grouping unreliable.

**Draft validation:**

- Flag null or blank department values.
- Flag department values outside the approved list.
- Flag casing, spacing, or naming variants.

### visit_type

**Draft rule:** Visit type values should use approved categories only.

**Why it matters:** Inconsistent visit types make operational reporting and trend analysis unreliable.

**Draft validation:**

- Flag visit types outside the approved list.
- Standardize known variants only after keeping an audit trail of the raw value.
