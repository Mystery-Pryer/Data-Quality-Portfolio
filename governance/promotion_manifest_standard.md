# Cross-Repository Promotion Manifest Standard

Every private-to-public evidence promotion must record: source repository and commit; destination repository and commit; selected files; sanitization performed; restriction/privacy review; approval; validation and result; date; operator; and residual risks.

Use `governance/promotion_manifest.csv`. Create a row before promotion with `destination_commit` set to `PENDING`, then update it after the destination commit is verified remotely. Never promote restricted sources, credentials, personal records, or unsupported claims.
