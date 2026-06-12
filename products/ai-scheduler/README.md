# AI Scheduler Agent — Architecture & API Patterns

Standalone conversational scheduling agent using Google Calendar REST API on Cloudflare Workers.

## Architecture

```
POST /chat  →  LLM (Gemini/OpenAI)  →  Tool: list_free_slots
                                    →  Tool: book_appointment
                                    →  Tool: cancel_appointment
                                    →  Google Calendar REST API
```

The LLM decides which tool to call based on the user's message. Each tool maps to a Google Calendar API endpoint via raw `fetch()` — no SDKs needed.

## Tool Definitions

### `list_free_slots`
- **What it does:** Queries Google Calendar freebusy API for available time windows within business hours
- **API used:** `POST https://www.googleapis.com/calendar/v3/freeBusy`
- **Returns:** Array of available time slots (start/end datetime)

### `book_appointment`
- **What it does:** Creates a calendar event at a confirmed time slot
- **API used:** `POST https://www.googleapis.com/calendar/v3/calendars/primary/events`
- **Returns:** Event ID + confirmation link

### `cancel_appointment`
- **What it does:** Deletes or updates an existing event
- **API used:** `DELETE https://www.googleapis.com/calendar/v3/calendars/primary/events/{eventId}`

## Key Pattern: SDK-Free Google Calendar

```typescript
// No googleapis package needed — just native fetch
async function getAccessToken(refreshToken: string, clientId: string, clientSecret: string): Promise<string> {
  const resp = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: clientId,
      client_secret: clientSecret,
      refresh_token: refreshToken,
      grant_type: "refresh_token",
    }),
  });
  const data = await resp.json<{ access_token: string }>();
  return data.access_token;
}
```

This pattern works on Cloudflare Workers out of the box. No module resolution issues, no wasm polyfills, no edge-case bugs.

## Authentication Flow

1. User authorizes via Google OAuth (one-time setup)
2. Refresh token stored as Worker secret
3. Each API call exchanges refresh token → access token → makes request
4. Access token cached in-memory until expiry (3600s)

## LLM Configuration Options

| Provider | Model | Cost/1M tokens | Tool Calling |
|----------|-------|----------------|--------------|
| Gemini | gemini-1.5-flash | $0.075 / $0.30 | Native (excellent) |
| OpenAI | gpt-4o-mini | $0.15 / $0.60 | Native (flawless) |
| DeepSeek | deepseek-chat | $0.14 / $0.28 | Native (good) |
| Groq | llama-3.1-8b-instant | $0.05 / $0.08 | Simulated (fair) |

---

👉 **[Get the full deployable template on Gumroad →](https://michaelforge0.gumroad.com/l/sitqsv)**  
Includes: complete TypeScript source, wrangler.toml, database adapter, README with OAuth walkthrough.
