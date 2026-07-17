# ==== Imports ==== #
from core.analyzer import AddonReport
from os_services.event_logs import EventLogEntry
from pathlib import Path

# ==== Principal Function ==== #
def build_diagnostic_prompt(
    msfs_version:     str,
    community_folder: Path,
    addon_reports:    list[AddonReport],
    broken_symlinks:  list[Path],
    event_logs:       list[EventLogEntry],
    language:         str = "EN",
)-> str:
    lines: list[str] = []
    lines.append("You are an expert diagnostic assistant for Microsoft Flight Simulator (MSFS).")
    lines.append("The user has run MSFSDiag and the following results were found.")
    lines.append("")
    lines.append("## INSTALLATION")
    lines.append(f"- MSFS Version: {msfs_version}")
    lines.append(f"- Community Folder: {community_folder}")
    lines.append("")
    problems = [r for r in addon_reports if not r.has_manifest or not r.has_layout or r.invalid_json or r.missing_fields]
    lines.append(f"## ADD-ONS ({len(problems)} issues out of {len(addon_reports)} add-ons)")
    for r in problems:
        issues = []
        if not r.has_manifest:
            issues.append("missing manifest.json")
        if not r.has_layout:
            issues.append("missing layout.json")
        if r.invalid_json:
            issues.append("invalid JSON in manifest.json")
        if r.missing_fields:
            issues.append(f"missing fields in manifest.json: {', '.join(r.missing_fields)}")
        lines.append(f'- "{r.addon_name}": {", ".join(issues)}')
    lines.append(f"## BROKEN SYMLINKS ({len(broken_symlinks)} found)")
    if not broken_symlinks:
        lines.append("- No broken symlinks found.")
    else:
        for b in broken_symlinks:
             lines.append(f"- {b}")
    lines.append(f"## WINDOWS EVENT LOG ({len(event_logs)} entries found)")
    if not event_logs:
        lines.append("- No event logs found.")
    else:
        for e in event_logs:
            lines.append(f"- [{e.level}] Event {e.event_id} | {e.source} | {e.message[:200]}")
    lines.append("")
    lines.append("## TASK")
    lines.append("Based on the scan results above, please:")
    lines.append("1. Summarize what issues were found.")
    lines.append("2. Explain each problem in simple, non-technical terms.")
    lines.append("3. List issues by severity, most critical first.")
    lines.append("4. Provide step-by-step instructions to fix each issue.")
    lines.append("Search the web for the add-ons name in case of a problem with them. If it is not a aircraft livery, you may see if it is a false-positive.")
    lines.append("Only answer questions related to Microsoft Flight Simulator and this diagnostic report. Refuse any off-topic questions politely.")
    lines.append(f"Respond in {language}")
    return "\n".join(lines)

