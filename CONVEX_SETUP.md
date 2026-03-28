# Convex Cloud Setup - Mission Control

## Current Status

✅ **Schemas Ready:** Tasks, Calendar, Memories, Content, Agents
✅ **API Layer Implemented:** `/src/lib/api.ts` (mock data + Convex-ready)
✅ **Frontend Connected:** Dashboard, Tasks pages using API layer
✅ **Mock Data Working:** Full functionality with local data

**When Convex is deployed:** Simply update `api.ts` to call Convex endpoints instead of mock.

---

## Quick Start (5 minutes)

### 1. Create Convex Project

```bash
cd /home/pablo/.openclaw/workspace/mission-control
npx convex auth
# Follow the prompts to link to Convex Cloud
```

Or manually:
1. Go to https://dashboard.convex.dev
2. Click "New Project"
3. Create project named "mission-control"
4. Copy your **Deployment URL**

### 2. Add to `.env.local`

```bash
# In mission-control/.env.local
CONVEX_DEPLOYMENT=<your-deployment-url>
CONVEX_URL=https://<your-deployment-url>
```

### 3. Push Schema to Cloud

```bash
cd /home/pablo/.openclaw/workspace/mission-control
npx convex deploy
```

This uploads:
- `convex/schema.ts` - Database structure
- `convex/tasks.ts` - Task CRUD
- `convex/memories.ts` - Memory search
- `convex/calendar.ts` - Calendar events

### 4. Update Mission Control Frontend

In `mission-control/src/lib/` create `convexClient.ts`:

```typescript
import { ConvexHttpClient } from "convex/browser";

const convexUrl = process.env.NEXT_PUBLIC_CONVEX_URL;
if (!convexUrl) {
  throw new Error("NEXT_PUBLIC_CONVEX_URL env var is not set");
}

export const convex = new ConvexHttpClient(convexUrl);
```

### 5. Update `.env.local` for Frontend

```bash
NEXT_PUBLIC_CONVEX_URL=https://<your-deployment-url>
```

### 6. Test Connection

```bash
curl https://<your-deployment-url>/api/tasks
```

---

## Features Ready to Connect

### Tasks
- **Create:** `convex/tasks.ts::create`
- **List:** `convex/tasks.ts::list`
- **Update:** `convex/tasks.ts::update`
- **Delete:** `convex/tasks.ts::deleteTask`

### Calendar
- **Create:** `convex/calendar.ts::create`
- **List:** `convex/calendar.ts::list`
- **Update:** `convex/calendar.ts::updateStatus`

### Memories
- **Create:** `convex/memories.ts::create`
- **List:** `convex/memories.ts::list`
- **Search:** `convex/memories.ts::search`

---

## Pricing

**Convex Cloud FREE Plan:**
- 1 Million queries/month (plenty for personal use)
- 50GB data
- Real-time syncing
- No credit card needed

---

## Next Steps After Setup

1. Connect frontend to Convex client
2. Replace mock data with real API calls
3. Enable real-time updates with `useQuery`
4. Deploy frontend to Vercel

---

**Status:** Schema ready, awaiting Convex Cloud signup
**Docs:** https://docs.convex.dev
