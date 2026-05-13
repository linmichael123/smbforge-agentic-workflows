# Media Assets — Screenshots to Add

This repo is designed to be copy-pasted as a GitHub README. The markdown and diagrams render beautifully on GitHub. **However, real screenshots make the repo come alive for hiring managers.**

Below are the specific screenshots you should take from your live system and how to name them.

---

## Required Screenshots

### 1. SMS Booking Conversation
**File:** `media/sms-booking-conversation.png`
**What to capture:** Open your phone (or the Telnyx dashboard) and show a real SMS conversation where a customer books an appointment. Best to show:
- Customer texts in → AI responds with available times
- Customer picks a time → AI confirms with details
- Shows the natural conversational flow

### 2. Telegram Owner Notification
**File:** `media/telegram-booking-notification.png`
**What to capture:** Show the Telegram notification the owner receives when a booking is made:
- "📅 New Booking" card
- Customer name and phone
- Time and date
- Any action buttons (Approve/Reschedule) if implemented

### 3. Telegram Escalation Alert
**File:** `media/telegram-escalation-alert.png`
**What to capture:** The escalation notification when a customer selects "After-hours emergency":
- "⚠️ ESCALATION" header
- Customer phone
- Reason
- Last messages preview

### 4. Admin Dashboard (Flags)
**File:** `media/admin-flags-dashboard.png`
**What to capture:** The `/api/admin/flags?reviewed=0` endpoint response showing:
- The quality monitoring system
- Flag types (stuck, escalation_unresolved, etc.)
- The review workflow

### 5. Voice AI Call Log
**File:** `media/voice-ai-call-log.png`
**What to capture:** Telnyx Voice AI dashboard showing:
- A completed call
- The AI assistant transcript
- Duration and outcome

### 6. Cold SMS Dashboard (Optional)
**File:** `media/cold-sms-dashboard.png`
**What to capture:** If you have a dashboard or log showing cold SMS sends:
- Batch send summary
- Successful delivery stats
- 10DLC compliance indicator

---

## Image Guidelines

| Specification | Value |
|--------------|-------|
| Format | PNG (screenshots), not JPEG |
| Width | 800-1200px (desktop) or phone-native (mobile) |
| DPI | 72 (standard web) |
| File size | Under 500KB each |
| Naming | `kebab-case-description.png` |
| Blur/Sensitive | Blur customer phone numbers and names if privacy is a concern |

---

## Adding to README

Once you add the screenshots to `/media/`, update `README.md` to reference them:

```markdown
## Screenshots

### SMS Booking Flow
![SMS Booking Conversation](media/sms-booking-conversation.png)

### Owner Notification (Telegram)
![Telegram Booking Notification](media/telegram-booking-notification.png)

### Escalation Alert
![Telegram Escalation Alert](media/telegram-escalation-alert.png)
```

---

## No Fake Data Policy

Do NOT create mockups or fake screenshots. Real product screenshots (even with blurred PII) are 10x more impressive for hiring managers than mockups. Take them from:
- **Your real phone** (SMS conversation screenshots)
- **Telnyx dashboard** (call logs, SMS history)
- **Cloudflare dashboard** (worker metrics, D1 queries)
- **Telegram app** (owner notifications)
- **API responses** (flags, conversations endpoints)
