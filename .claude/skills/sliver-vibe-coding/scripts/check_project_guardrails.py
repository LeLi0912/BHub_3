#!/usr/bin/env python3
"""Check whether a user project has the minimum Sliver Vibe Coding guardrails."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_FILES_BY_MODE = {
    "bootstrap": [
        "AGENTS.md",
        "{truth_dir}/README.md",
        "{truth_dir}/project-brief.md",
        "{truth_dir}/architecture.md",
        "{truth_dir}/acceptance.md",
    ],
    "adoption": [
        "AGENTS.md",
        "{truth_dir}/README.md",
        "{truth_dir}/current-state-audit.md",
        "{truth_dir}/architecture.md",
        "{truth_dir}/acceptance.md",
    ],
    "constitution": [
        "AGENTS.md",
    ],
}

REQUIRED_LINKS_BY_MODE = {
    "bootstrap": [
        "project-brief.md",
        "architecture.md",
        "acceptance.md",
    ],
    "adoption": [
        "current-state-audit.md",
        "architecture.md",
        "acceptance.md",
    ],
}

REQUIRED_HEADINGS = {
    "AGENTS.md": [
        "##",
    ],
    "README.md": [
        "## 当前真源索引",
        "## 文档职责",
        "## 更新规则",
    ],
    "project-brief.md": [
        "## 项目边界",
        "## 第一闭环",
        "## 不做什么",
        "## 验收标准",
        "## 停止条件",
    ],
    "current-state-audit.md": [
        "## 现状证据",
        "## 产品边界",
        "## 调用链和 owner",
        "## 危险接管动作",
        "## 下一步",
    ],
    "architecture.md": [
        "## 推荐架构",
        "## Owner Map",
        "## 禁止路径",
        "## 验证方式",
    ],
    "acceptance.md": [
        "## 验收门禁",
        "## 证据记录",
        "## 停止条件",
        "## 漂移检查",
    ],
}

REQUIRED_SNIPPETS_BY_MODE = {
    "bootstrap": {
        "AGENTS.md": [
            "架构优先",
            "设计优先",
            "真源",
            "停止条件",
            "未验证",
        ],
        "project-brief.md": [
            "第一闭环",
            "不做什么",
            "停止条件",
        ],
        "architecture.md": [
            "推荐架构",
            "Owner Map",
            "禁止路径",
        ],
        "acceptance.md": [
            "验收门禁",
            "证据记录",
            "漂移检查",
        ],
    },
    "adoption": {
        "AGENTS.md": [
            "半路接管",
            "危险接管动作",
            "禁止 `git add .`",
        ],
        "current-state-audit.md": [
            "现状证据",
            "技术栈适配",
            "危险接管动作",
        ],
        "architecture.md": [
            "当前 owner",
            "应该 owner",
            "禁止 owner",
        ],
        "acceptance.md": [
            "第一个安全任务",
            "漂移检查",
        ],
    },
    "constitution": {
        "AGENTS.md": [
            "架构优先",
            "真源",
            "停止条件",
            "未验证",
        ],
    },
}

PLACEHOLDER_MARKERS = [
    "待填写",
    "TODO",
    "TBD",
    "@@",
    "<Project>",
    "<project>",
]

DRIFT_MARKERS = [
    "后续再补",
    "先留着",
    "暂时兼容",
    "临时兼容",
    "以后再说",
    "later maybe",
]

NEGATED_MARKER_TERMS = [
    "禁止",
    "不得",
    "不能",
    "不要",
    "Do not",
    "Never",
]

PRIVATE_RISK_NAMES = [
    ".env",
    ".env.local",
    "id_rsa",
    "service-account",
    "secret",
    "secrets",
    "private-key",
    "database.sql",
    "dump.sql",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="replace")


def rel_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def doc_key(rel: str, truth_dir: str) -> str:
    prefix = f"{truth_dir}/"
    if rel.startswith(prefix):
        return rel[len(prefix) :]
    return rel


def required_files(mode: str, truth_dir: str) -> list[str]:
    return [item.format(truth_dir=truth_dir) for item in REQUIRED_FILES_BY_MODE[mode]]


def is_empty_field(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("- ") or ":" not in stripped:
        return False
    key, value = stripped[2:].split(":", 1)
    return bool(key.strip()) and not value.strip()


def is_negated_line(line: str) -> bool:
    return any(term in line for term in NEGATED_MARKER_TERMS)


def find_private_risks(root: Path) -> list[str]:
    risks: list[str] = []
    for child in root.rglob("*"):
        if ".git" in child.parts:
            continue
        name = child.name.lower()
        if any(marker in name for marker in PRIVATE_RISK_NAMES):
            risks.append(rel_path(child, root))
            if len(risks) >= 30:
                break
    return risks


def check_stage_file(root: Path, stage_file: str | None) -> dict:
    result = {
        "stage_file": stage_file,
        "missing_stage_file": False,
        "missing_stage_headings": [],
        "stage_placeholders": [],
    }
    if not stage_file:
        result["missing_stage_file"] = True
        return result

    path = root / stage_file
    if not path.exists():
        result["missing_stage_file"] = True
        return result

    text = read_text(path)
    heading_groups = {
        "阶段目标 / Stage goal": ["Stage goal", "阶段目标"],
        "范围 / Scope": ["Scope", "范围"],
        "不做什么 / Non-goals": ["Non-goals", "不做什么"],
        "验证 / Validation": ["Validation", "验证"],
        "停止条件 / Stop": ["Stop", "停止条件"],
        "未验证": ["未验证", "Unverified"],
    }
    for group, aliases in heading_groups.items():
        if not any(alias in text for alias in aliases):
            result["missing_stage_headings"].append(group)

    for marker in PLACEHOLDER_MARKERS:
        if marker in text:
            result["stage_placeholders"].append({"file": stage_file, "marker": marker})
    return result


def check_project(
    root: Path,
    mode: str,
    truth_dir: str,
    allow_template: bool,
    stage_file: str | None,
    skip_private_scan: bool,
) -> dict:
    missing_files: list[str] = []
    missing_headings: list[dict[str, str]] = []
    missing_snippets: list[dict[str, str]] = []
    missing_links: list[str] = []
    placeholders: list[dict[str, str]] = []
    empty_fields: list[dict[str, int | str]] = []
    drift_markers: list[dict[str, int | str]] = []

    if mode == "stage":
        stage_result = check_stage_file(root, stage_file)
        failures = []
        if stage_result["missing_stage_file"]:
            failures.append("missing_stage_file")
        if stage_result["missing_stage_headings"]:
            failures.append("missing_stage_headings")
        if stage_result["stage_placeholders"] and not allow_template:
            failures.append("stage_placeholders")
        return {
            "root": str(root),
            "mode": mode,
            "truth_dir": truth_dir,
            "ok": not failures,
            "failures": failures,
            **stage_result,
        }

    for rel in required_files(mode, truth_dir):
        path = root / rel
        if not path.is_file():
            missing_files.append(rel)
            continue

        text = read_text(path)
        key = doc_key(rel, truth_dir)
        for heading in REQUIRED_HEADINGS.get(key, []):
            if heading not in text:
                missing_headings.append({"file": rel, "heading": heading})
        for snippet in REQUIRED_SNIPPETS_BY_MODE.get(mode, {}).get(key, []):
            if snippet not in text:
                missing_snippets.append({"file": rel, "snippet": snippet})
        for marker in PLACEHOLDER_MARKERS:
            if marker in text:
                placeholders.append({"file": rel, "marker": marker})
        for line_no, line in enumerate(text.splitlines(), start=1):
            if is_empty_field(line):
                empty_fields.append({"file": rel, "line": line_no, "field": line.strip()[2:]})
            for marker in DRIFT_MARKERS:
                if marker in line and not is_negated_line(line):
                    drift_markers.append({"file": rel, "line": line_no, "marker": marker})

    readme_path = root / truth_dir / "README.md"
    if readme_path.exists() and mode in REQUIRED_LINKS_BY_MODE:
        readme = read_text(readme_path)
        for link in REQUIRED_LINKS_BY_MODE[mode]:
            if link not in readme:
                missing_links.append(link)

    private_risks = [] if skip_private_scan else find_private_risks(root)

    failures: list[str] = []
    if missing_files:
        failures.append("missing_required_files")
    if missing_headings:
        failures.append("missing_required_headings")
    if missing_snippets:
        failures.append("missing_required_snippets")
    if missing_links:
        failures.append("truth_readme_missing_links")
    if placeholders and not allow_template:
        failures.append("placeholder_markers")
    if empty_fields and not allow_template:
        failures.append("empty_required_fields")
    if drift_markers and not allow_template:
        failures.append("drift_markers")

    return {
        "root": str(root),
        "mode": mode,
        "truth_dir": truth_dir,
        "ok": not failures,
        "failures": failures,
        "missing_required_files": missing_files,
        "missing_required_headings": missing_headings,
        "missing_required_snippets": missing_snippets,
        "truth_readme_missing_links": missing_links,
        "placeholder_markers": placeholders,
        "empty_required_fields": empty_fields,
        "drift_markers": drift_markers,
        "private_risk_names": private_risks,
        "private_risk_note": "informational only; inspect before staging or pushing",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", help="Project root to check")
    parser.add_argument(
        "--mode",
        choices=["bootstrap", "adoption", "constitution", "stage"],
        default="bootstrap",
        help="Guardrail mode to run",
    )
    parser.add_argument(
        "--truth-dir",
        default="dev-docs",
        help="Internal truth-document directory, default: dev-docs",
    )
    parser.add_argument(
        "--stage-file",
        help="Stage implementation truth file, used with --mode stage",
    )
    parser.add_argument(
        "--allow-template",
        action="store_true",
        help="Allow placeholders and empty fields when checking bundled templates",
    )
    parser.add_argument(
        "--skip-private-scan",
        action="store_true",
        help="Skip filename-based private material scan",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON only")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists():
        print(f"FAIL: project root does not exist: {root}", file=sys.stderr)
        return 2

    result = check_project(
        root=root,
        mode=args.mode,
        truth_dir=args.truth_dir,
        allow_template=args.allow_template,
        stage_file=args.stage_file,
        skip_private_scan=args.skip_private_scan,
    )

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["ok"] else 1

    print(f"{'OK' if result['ok'] else 'FAIL'}: {root}")
    print(f"mode: {result['mode']}")
    print(f"truth_dir: {result['truth_dir']}")
    for key, value in result.items():
        if key in {"root", "mode", "truth_dir", "ok"}:
            continue
        if value:
            print(f"{key}: {json.dumps(value, ensure_ascii=False)}")

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
