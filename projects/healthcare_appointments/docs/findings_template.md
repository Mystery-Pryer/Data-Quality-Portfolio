# Findings Template

Use this template when turning a data quality issue into a stakeholder-ready finding.

## Ticket / Finding Name

Short name or issue ID:

## Business Question

What question are we trying to answer?

## DQ Dimension

Completeness, validity, conformity, integrity, uniqueness, timeliness, consistency, or another agreed dimension:

## Business Rule

What should be true if the data is correct or usable?

## Scope / Population

Which rows are included before measuring the defect?

Example:

```text
All appointment records
Completed appointment records only
Records from a specific facility, department, or date range
```

## Defect Definition

What exact condition makes a row fail the rule?

## Evidence Source

Reference the evidence used:

```text
SQL query
pandas output
cleaned CSV
flagged review CSV
record count
percentage
sample records
```

## Evidence Summary

- Affected record count:
- Affected percentage, if available:
- Affected group, if available:
- Sample evidence file:

## Interpretation

What does the evidence mean?

## Impact

What workflow, report, decision, or metric may become unreliable?

## Recommendation

Recommended action:

```text
Confirm rule
Clean values
Backfill values
Fix source entry
Add validation control
Create monitoring check
Exclude from reporting until reviewed
```

## Validation Plan

How will the rule or fix be tested?

## Open Questions

What still needs confirmation from the business owner, data owner, or source-system owner?

## Limitations

Known limits of the analysis:
