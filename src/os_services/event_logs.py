# ==== Imports ==== #
import win32evtlog

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
    entries = []

    try:
        log = win32evtlog.OpenEventLog(None, "Application")
    except Exception:
        return []

    try:
        events = win32evtlog.ReadEventLog(
            log,
            win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ,
            0,
        )

        for event in events:
            source = event.SourceName
            if "flight simulator" not in source.lower():
                continue

            entries.append(EventLogEntry(
                source    = source,
                event_id  = event.EventID,
                level     = str(event.EventType),
                message   = str(event.StringInserts),
                timestamp = event.TimeGenerated.replace(tzinfo=None),
            ))

            if len(entries) >= max_entries:
                break
    finally:
        win32evtlog.CloseEventLog(log)

    return entries
