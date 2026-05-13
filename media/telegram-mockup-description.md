# Telegram Owner Experience — Mockup Description

This file describes the Telegram bot interface that business owners use as their central command center. Screenshots of the actual Telegram chat would go here (see `README.md` in this directory for screenshot instructions).

## Owner Bot Capabilities

The Telegram bot gives the business owner **full control over their AI assistant** without needing a dashboard or web interface.

### Core Commands

| Command | Function |
|---------|----------|
| `/approve` | Approve pending booking or order |
| `/schedule` | View today's appointments |
| `/cancel` | Cancel or reschedule an appointment |
| `/status` | Quick system health check |
| `/leads` | View recent leads and their status |
| `/campaign` | Start a broadcast campaign (Max plan) |
| `/review` | Manage online review requests |
| `/invoice` | View or send an invoice |

### Real-Time Notifications

The bot proactively pushes notifications to the owner:

```
📅 New Booking Approved
Customer: Mike's Plumbing
Time: Today, 2:00 PM
Service: Emergency pipe repair
Booked via: SMS (customer-initiated)
→ Automatically synced to Google Calendar

[View] [Reschedule] [Cancel]
```

```
⚠️ ESCALATION — Urgent
From: (714) 555-1234
Reason: Emergency call after hours
Agent: "Let me connect you with the owner..."

→ Customer is waiting. Reply here to message them.
```

```
🛒 New Order
Customer: Jane's Cleaning Co.
Plan: Max ($199/mo + $299 setup)
Ordered: 15 min ago

[Approve] [Contact Customer] [View Details]
```

### Owner Approval Workflow

1. Booking/order comes in → system sends Telegram notification
2. Owner taps **Approve** → system finalizes the action
3. Owner taps **Modify** → bot asks what to change
4. Owner taps **Decline** → bot asks for reason → customer notified

This human-in-the-loop pattern is critical for:
- **Trust**: The owner is never surprised by a booking
- **Quality**: The AI catches 90% of cases correctly; the owner handles the edge cases
- **Training**: Owner corrections become implicit training data for the AI

### Why Telegram Instead of a Mobile App?

| Factor | Telegram Bot | Native Mobile App |
|--------|-------------|-------------------|
| Development cost | $0 (existing platform) | $20K-$50K |
| Install friction | 0 (they already have Telegram) | Must download + sign up |
| Push notifications | Native | Must implement |
| Rich UI | Inline keyboards, buttons | Full control |
| Cross-platform | iOS + Android + Desktop | One platform at a time |
| Updates | Instant (bot code deploy) | App Store review cycle |
| Owner adoption | Very high (tradespeople use WhatsApp/Telegram) | Low (app fatigue) |
