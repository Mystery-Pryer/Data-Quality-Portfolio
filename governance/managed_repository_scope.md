# Managed Repository Scope

Managed DQE repositories: `Career-Operations`, `Data-Quality`, `Data-Quality-Portfolio`, `Funnel-Analytics-Mini-Project`, `peptide-systems-lab`, `repo-automation`, and `awesome-data-quality`.

Reference/upstream repositories: `awesome`, `fg-data-profiling`, and `pandas_dq`. Do not apply DQE policies, automation, formatting, or commits to them unless the user explicitly changes their classification.

Safety, privacy, authorization, and non-destructive constraints always govern. Current explicit user intent governs intended changes. Verified remote state governs facts, history, and progress. Committed policies and task contracts govern execution unless deliberately changed.

If a checkout is dirty, fetch and inspect without altering it. When safe, create an isolated Git worktree from the verified remote default branch. Never reset, rebase, force-push, auto-stash, overwrite, discard, or silently merge existing work.
