# Context Handoff

Use this when the conversation is too large, the user wants to continue in a new window, another agent will take over, or a stage is not fully closed.

The handoff must be copy-paste-ready. It should preserve current truth, not merely summarize what the agent feels was done.

## Required Contents

Include:

- Project path, current date, branch, and target environment.
- Hard instructions to preserve: language, AGENTS.md, truth root, no patching, no destructive actions, no deployment without approval.
- Git status for every relevant repo, including nested internal-doc repos.
- Latest commits for every relevant repo.
- Current source-truth documents.
- Work completed in this window, grouped by owner layer.
- Files changed but not committed.
- Validation evidence: exact commands and pass/fail result.
- Runtime state: running services, ports, URLs, stale process warnings, deploy/device state when relevant.
- Current architecture/product boundary and rejected routes.
- Known risks, blocked evidence, and unresolved user decisions.
- Drift warnings: what the next agent must not do.
- Exact next safest commands or next action.

## Handoff Shape

Use this structure:

```markdown
# <Project> 新窗口交接

工作目录：
当前日期：
当前目标：

必须遵守：
- ...

## Git State

主仓：
```text
...
```

内部文档仓，如果存在：
```text
...
```

## Current Truth

- 产品边界：
- 当前阶段：
- 主要 owner：
- 当前真源文档：
- 用户确认过的非目标：
- 被拒绝路线：

## 本窗口完成

### <owner layer / feature area>
- ...

## 变更文件

- ...

## 验证证据

已通过：
```bash
...
```

未运行 / 未验证：
- ...

## 运行状态

- ...

## 漂移警告

- 不要 ...
- 保持 ...

## 下一步

1. ...
2. ...
```

## Rules

- Do not omit dirty or untracked files.
- Do not say "all passed" without commands and results.
- Do not omit nested repo state.
- Do not hide missing evidence; mark it `未验证`.
- Do not give a generic continuation prompt. The next agent must be able to act from paths, files, commands, and boundaries.
- If suggesting a commit, use explicit pathspecs. Never suggest `git add .`.
