# Changelog

## Unreleased

- Integrated bootstrap/adoption project templates into the public `sliver-vibe-coding` skill so empty and half-built projects can materialize usable truth docs without a second workflow skill.
- Strengthened Git safety rules so remote URL configuration is separate from push approval, credentials are never requested in chat, and rollback/reset/restore requests require a loss audit before destructive commands.
- Added a mixed-commit revert gate: rollback requests now require intent classification and file/hunk ownership review before any whole-commit revert, with atomic commit grouping guidance for future checkpoints.
- Added task-level finding severity guidance for `阻断问题`, `设计风险`, `可记录债务`, and `无关优化` so ordinary work is not over-governed while real safety/data/owner blockers remain blocking.
- Added `scripts/check_project_guardrails.py` for structural checks of user-project governance artifacts, including bootstrap, adoption, constitution, and stage truth modes.
- Added `/上下文交接` and `references/context-handoff.md` for copy-paste-ready new-window or agent-to-agent handoffs.
- Strengthened feature execution, rescue, and validation references with owner-layer execution order, non-trivial bug evidence ladders, git/upstream checks, hypothesis tables, regression gates, and evidence-plane verdicts.
- Reworked route evaluation so cases are inferred from the actual `user` prompt against automatic triggers, and expanded coverage to 48 natural-language cases across every route label.
- Added platform-capability, frontend design-system, single-runtime, and cross-language architecture gates for technical selection.
- Required blocking questions before final stack selection when desktop/local system automation, browser extension, background worker, or hybrid capability is unclear.
- Required `Cross-Language Architecture Truth` before recommending multiple backend runtimes/languages.
- Clarified that this is a project-governance skill, not a deep engineering execution skill.
- Added lightweight skill-fit assessment for ordinary bug fixes, local UI tweaks, single-file edits, test/build fixes, and code review before escalating into governance.
- Added `普通工程任务` to task risk gates so ordinary engineering work can proceed with narrow inspection, targeted fixes, and proportional validation.
- Expanded route evaluation coverage from 9 smoke cases to 18 lightweight behavior-regression cases, including ordinary engineering tasks and governance escalation scenarios.
- Documented that route tests are lightweight behavior regression checks, not a full substitute for human evaluation.

## 0.1.0 - 2026-06-20

- Added narrowed trigger scope for non-technical project governance, adoption, rescue, truth documents, validation, release, and constitution work.
- Split route procedures out of the former monolithic `references/commands.md` into focused route references.
- Added task risk gates for `轻量任务`, `标准任务`, and `高风险任务`.
- Added local validation and route regression scripts with no third-party Python dependencies.
- Added HTTPS install path, compatibility notes, and version governance.
