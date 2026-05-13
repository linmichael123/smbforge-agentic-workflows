# Telegram Escalation Logic

How the system routes critical conversations to the business owner via Telegram.

## When Escalation Fires

The system escalates in three scenarios:

### 1. Customer-Initiated (Journey 3 — After-Hours Emergency)

When a customer selects "After-hours emergencies" or mentions an urgent situation:

```
Customer: "3" or "My pipe burst" or "I have an emergency"

Agent Action (deterministic, not LLM-decided):
1. Call escalate_to_owner() → sets conversation status to 'escalated'
2. Persists escalation_reason to D1
3. Returns: "Let me connect you with our team. They'll reach out shortly."
4. Telegram notification to owner within 30 seconds
```

**Evolution:** In V1, the LLM was told to "ask what the emergency is first." It chatted instead of escalating. V2 made escalation the FIRST action — before responding to the customer.

### 2. Trigger-Detected (Rule-Based)

During any conversation, if the LLM detects an escalation trigger:

```
Escalation Triggers (hard-coded in system prompt):
- Customer asks about pricing negotiations or discounts
- Customer expresses strong frustration or dissatisfaction
- Customer requests custom work beyond standard packages
- Contract or legal questions
- Customer explicitly asks to speak to a human/owner/manager
- Any request over $1,000
```

### 3. System-Detected (Quality Monitor)

The hourly cron checks all `escalated` conversations. If an escalation has been pending for 2+ hours without owner response:

```
1. Creates a conversation_flags entry (type: escalation_unresolved)
2. Deduplication: only one unreviewed flag per conversation
3. Next cron cycle: if still unresolved, dedup keeps it from re-firing
4. Owner reviews via GET /api/admin/flags?reviewed=0
```

## Telegram Notification Format

When an escalation fires, the owner receives:

```
⚠️ ESCALATION — Customer Name
📞 (555) 123-4567

Reason: After-hours emergency

Last messages:
- Customer: "3"
- Agent: "Let me connect you with our team..."

[Review] GET /api/admin/flags?reviewed=0
[Convo] GET /api/admin/conversations?id=126
```

The notification includes:
- Customer phone number (click-to-call on mobile)
- Escalation reason
- Last 3 messages for context
- Admin API endpoints for review

## Owner Response

The owner can:
1. **Call the customer back** — phone is in the notification
2. **Respond via Telegram** — the bot forwards messages to the customer
3. **Mark as reviewed** — via admin API, which suppresses further escalation flags

## Escalation State Machine

```
NEW → ACTIVE → (customer triggers escalation) → ESCALATED
                                                  ↓
                                         Owner notified via Telegram
                                                  ↓
                                         (owner reviews within 2h)
                                                  ↓
                                   Owner responds? ── Yes → RESOLVED
                                        │
                                        No (2h+)
                                        ↓
                                   Flag created (escalation_unresolved)
                                        │
                                   Still unresolved at next cron?
                                        │
                                   Dedup prevents re-flagging
                                   (only 1 unreviewed flag per conversation)
```

## Deduplication Design

**Problem:** The hourly cron creates a new flag every cycle if the owner hasn't reviewed. 10+ identical flags for the same conversation.

**Fix:** `alreadyFlagged()` checks for **any unreviewed flag** of the same type for that conversation — regardless of age. Once reviewed, the conversation's escalation status is acknowledged and no more flags fire.
