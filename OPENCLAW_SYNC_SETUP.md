# OpenClaw API Sync - Mission Control Integration

## What's Syncing

✅ **Cron Jobs → Calendar**
- Automatically pulls your OpenClaw cron jobs
- Shows next execution time
- Updates enabled/disabled status
- Runs every 1 hour

✅ **Manual Sync**
- Button in Calendar page: "🔄 Sync Now"
- Fetches latest jobs instantly

✅ **Auto-logging**
- Each sync event logged to `facts.jsonl`
- Tracked for memory

---

## How It Works

```
OpenClaw CLI
    ↓
openclaw cron list --json
    ↓
sync_openclaw_to_mission.py
    ↓
openclaw_calendar_sync.jsonl
    ↓
/api/calendar/sync (endpoint)
    ↓
Mission Control Calendar page
```

---

## Cron Job

**Name:** `sync_openclaw_calendar`
**Schedule:** Every hour (0 * * * *)
**File:** `/home/pablo/sync_openclaw_to_mission.py`

Automatic - no setup needed.

---

## Current Synced Jobs (4 total)

1. **rebuild_memory_index** - Every 3h +30min
2. **extract_memory_facts** - Every 3h
3. **inject_memory_prompt** - Every 3h +15min
4. **init_daily_memory** - Daily at midnight

All visible in http://localhost:3000/calendar

---

## Manual Sync

```bash
# Trigger instantly
python3 /home/pablo/sync_openclaw_to_mission.py

# Or via API
curl -X POST http://localhost:3000/api/calendar/sync
```

---

## Next: Task Updates from Cron

When Convex is live, you can:
- Mark cron job as "DONE" → Auto-update calendar
- Create task "Run cron X" → Gets scheduled
- Bidirectional sync (tasks ↔ cron)

---

**Status:** ✅ Live and syncing
**API:** `/api/calendar/sync` (GET to list, POST to sync)
