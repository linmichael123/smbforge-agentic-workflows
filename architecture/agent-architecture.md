# Multi-Agent Architecture

Breakdown of the autonomous agent system, agent roles, and how they collaborate.

```mermaid
flowchart TD
    subgraph External["External Interfaces"]
        SMS["📱 SMS<br/>Telnyx Webhook"]
        VOICE["🎙️ Voice AI<br/>Telnyx Voice Assistant"]
        WEB["🌐 Website<br/>smbforge.com"]
        TEL["💬 Telegram Bot<br/>Owner Interface"]
    end

    subgraph AgentLayer["Agent Layer"]
        ORCH["Orchestrator Agent<br/>─────────────<br/>- Intent routing<br/>- System prompt assembly<br/>- Tool dispatch<br/>- Context management"]
        
        SMSAGENT["SMS Conversation Agent<br/>─────────────<br/>- Natural language understanding<br/>- Multi-language support<br/>- 3-journey navigation<br/>- Response generation"]
        
        VOICEAGENT["Voice Conversation Agent<br/>─────────────<br/>- Real-time speech<br/>- Deepgram transcription<br/>- Dynamic skill variables<br/>- Escalation detection"]
        
        ONAGENT["Onboarding Agent<br/>─────────────<br/>- Business info collection<br/>- Skill file generation<br/>- Stripe checkout flow<br/>- Phone provisioning"]
    end

    subgraph ToolLayer["Tool Execution Layer"]
        GCAL["Google Calendar<br/>─────────────<br/>check_availability()<br/>book_appointment()"]
        
        STRIPE["Stripe<br/>─────────────<br/>Payment links<br/>Subscriptions"]
        
        TELNYX["Telnyx<br/>─────────────<br/>SMS send/receive<br/>Voice routing"]
        
        GSHEETS["Google Sheets<br/>─────────────<br/>Invoice tracking<br/>Lead management"]
        
        DB["D1 Database<br/>─────────────<br/>Conversations<br/>Leads<br/>Flags<br/>Reviews"]
        
        KV["KV Store<br/>─────────────<br/>Client skills<br/>Config<br/>Session state"]
    end

    subgraph QualityLayer["Quality & Monitoring"]
        QMON["Quality Monitor<br/>─────────────<br/>- Flag stuck conversations<br/>- Detect unresponsive bot<br/>- Escalation tracking<br/>- Hourly cron checks"]
        
        NOTIFY["Notification System<br/>─────────────<br/>- Platform alerts<br/>- Daily reviews<br/>- Weekly summaries"]
        
        AUDIT["Security Audit<br/>─────────────<br/>- Auth check<br/>- PII redaction<br/>- Rate limiting"]
    end

    SMS --> SMSAGENT
    VOICE --> VOICEAGENT
    WEB --> ONAGENT
    TEL --> ORCH
    
    SMSAGENT --> ORCH
    VOICEAGENT --> ORCH
    ONAGENT --> ORCH
    
    ORCH --> GCAL
    ORCH --> STRIPE
    ORCH --> GSHEETS
    ORCH --> DB
    ORCH --> KV
    
    QMON --> DB
    QMON --> NOTIFY
    
    style ORCH fill:#7b1fa2,stroke:#4a0072,color:#fff
    style SMSAGENT fill:#0288d1,stroke:#01579b,color:#fff
    style VOICEAGENT fill:#0288d1,stroke:#01579b,color:#fff
    style ONAGENT fill:#0288d1,stroke:#01579b,color:#fff
    style QMON fill:#f57c00,stroke:#e65100,color:#fff
    style NOTIFY fill:#f57c00,stroke:#e65100,color:#fff
```

## Agent Responsibilities

### Orchestrator Agent
The central routing layer. It doesn't generate customer-facing responses — it routes intent to the right sub-agent and dispatches tools. Built with a system prompt that includes client configuration, escalation rules, and capability definitions.

**Key behaviors:**
- Assembles context from KV (client skill, config flags, pending items)
- Routes between SMS, voice, and onboarding sub-agents
- Manages CONVERSATION_LIMITS (nudge at 8 turns, direct at 12)
- Handles journey switching cleanly (abandons previous journey)

### SMS Conversation Agent
The customer-facing text agent. Handles the full 3-journey model with Gemini native function calling.

**Journeys:**
| Journey | Trigger | Flow |
|---------|---------|------|
| **Booking** | "Book a demo" / "I need a quote" | Check availability → present slots → collect name/email → book → confirm |
| **Ordering** | "Sign me up" / "Pricing" | Present plans → recommend → parse order → collect info → submit |
| **Escalation** | "Emergency" / "I want to cancel" | Escalate immediately → Telegram notification → owner handles |

### Voice Conversation Agent
Handles inbound phone calls via Telnyx Voice AI. Uses Claude Haiku for conversation + Deepgram for transcription + natural-sounding TTS.

**Configuration:**
- Dynamic skill variables loaded per client
- Escalation triggers parsed from client skill files
- Noise suppression (Krisp)
- Speed: 0.93x for natural pacing

### Quality Monitor
Runs on an hourly cron to detect and flag issues:

| Flag Type | Detects | Action |
|-----------|---------|--------|
| `bot_unresponsive` | Bot didn't reply to customer in 15+ min | Critical alert to platform |
| `stuck` | Conversation idle 24h with no resolution | Auto-resolved, warning flag |
| `escalation_unresolved` | Escalation pending 2+ hours | Recurring warning (deduplicated) |
| `safety_gate` | Outreach sending at 0% reply rate | Auto-pause pipeline |

## Conversation Lifecycle

```
NEW → [Greeting + Menu] → ACTIVE → [Journey in progress]
                                      ↓
                              RESOLVED (successful booking/order)
                                      ↓
                              ESCALATED (sent to owner via Telegram)
                                      ↓
                              RESOLVED (owner handled it)
                                      ↓
                              AUTO-RESOLVED (24h idle)
```

Each transition is logged to D1 with full message history for audit and analysis.
