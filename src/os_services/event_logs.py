# ==== Imports ==== #
import subprocess
import json
from dataclasses import dataclass
from datetime import datetime


# ==== Event Log Entry ==== #
@dataclass
class EventLogEntry:
    source:    str
    event_id:  int
    level:     str
    message:   str
    timestamp: datetime


# ==== Event Log Reading ==== #
def get_msfs_events(max_entries: int = 50) -> list[EventLogEntry]:
    # Usa PowerShell para ler os Event Logs sem dependências externas
    ps_command = f"""
    Get-EventLog -LogName Application -Newest {max_entries} |
    Where-Object {{ $_.Source -match 'flight simulator' }} |
    Select-Object Source, EventID, EntryType, Message, TimeGenerated |
    ConvertTo-Json -Compress
    """

    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", ps_command],
            capture_output=True,
            text=True,
            timeout=15,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return []

        data = json.loads(result.stdout)

        # PowerShell devolve um objeto em vez de lista se só houver 1 resultado
        if isinstance(data, dict):
            data = [data]

        entries = []
        for item in data:
            entries.append(EventLogEntry(
                source    = item.get("Source", ""),
                event_id  = item.get("EventID", 0),
                level     = str(item.get("EntryType", "")),
                message   = str(item.get("Message", "")),
                timestamp = datetime.fromisoformat(item.get("TimeGenerated", "1970-01-01")),
            ))

        return entries

    except Exception:
        return []
