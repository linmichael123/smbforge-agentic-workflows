# Customer Workflow Diagram

Full end-to-end flow of a customer interaction with SMB Forge's autonomous agent system.

```mermaid
flowchart TD
    subgraph Initiation["1. Contact Initiation"]
        A["Customer calls or texts<br/>(949) 565-1908"] --> B["Telnyx receives<br/>inbound SMS/call"]
    end

    subgraph Identification["2. Client Resolution"]
        B --> C["Telnyx webhook →<br/>Cloudflare Worker"]
        C --> D{"Is this number<br/>mapped to a client?"}
        D -->|"Yes"| E["Load client skill file<br/>from KV storage"]
        D -->|"No / smb-forge"| F["Load default<br/>SMB Forge configuration"]
    end

    subgraph AgentConversation["3. AI Conversation"]
        E --> G["Build system prompt<br/>with client context + tools"]
        F --> G
        G --> H["LLM orchestrator<br/>routes conversation"]
        H --> I{"Intent detection<br/>LLM classifies request"}
    end

    subgraph IntentRouting["4. Intent Routing"]
        I -->|"1. Book a Demo"| J1["Journey: Booking<br/>check_availability → present slots"]
        I -->|"2. Order a Product"| J2["Journey: Ordering<br/>parse_order → submit_order"]
        I -->|"3. After-Hours Emergency"| J3["Journey: Escalation<br/>escalate_to_owner"]
        I -->|"Other questions"| J4["Journey: Info<br/>get_business_info → steer to one of 3"]
    end

    subgraph ToolExecution["5. Tool Execution"]
        J1 --> K1["check_availability()<br/>Google Calendar API"]
        K1 --> L1["Present slots →<br/>Customer selects time"]
        L1 --> M1["book_appointment()<br/>Google Calendar write-back"]
        J2 --> K2["parse_order()<br/>Structured plan extraction"]
        K2 --> L2["Collect name + email<br/>→ submit_order()"]
        L2 --> M2["Order stored in D1<br/>→ Invoice generated"]
        J3 --> K3["escalate_to_owner()<br/>Status: escalated"]
        K3 --> L3["Telegram notification<br/>to business owner"]
        J4 --> M4["Answer question →<br/>Steer to journey 1, 2, or 3"]
    end

    subgraph OwnerReview["6. Owner Review (Human-in-the-Loop)"]
        M1 --> N["Telegram notification<br/>'New booking pending approval'"]
        M2 --> N
        N --> O["Owner reviews via<br/>Telegram bot commands"]
        O --> P{"Owner approves?"}
        P -->|"Yes"| Q["Execute action<br/>→ SMS confirmation"]
        P -->|"No"| R["Owner edits/rejects<br/>→ Customer notified"]
    end

    subgraph Confirmation["7. Customer Confirmation"]
        Q --> S["SMS or call back<br/>to customer"]
        R --> S
        S --> T["Conversation resolved<br/>or escalated"]
    end

    style A fill:#e1f5fe,stroke:#0288d1,color:#000
    style H fill:#f3e5f5,stroke:#7b1fa2,color:#000
    style I fill:#fff3e0,stroke:#f57c00,color:#000
    style N fill:#fff3e0,stroke:#f57c00,color:#000
    style Q fill:#e8f5e9,stroke:#388e3c,color:#000
```

## Key Design Decisions

### Why SMS-First? 
Service business owners are on job sites — they can't stare at a dashboard. SMS is the only channel that works in a crawlspace, on a roof, or with wet hands. Telegram provides the owner interface when they take a break.

### Why LLM-Native Routing?
Traditional IVR trees ("Press 1 for...") have <20% completion rates for trades. An LLM that understands "My pipe burst" vs "How much for a water heater?" routes naturally without forcing customers through menus.

### Why Human-in-the-Loop?
Autonomy is the goal, but the owner knows their business. Escalation triggers (pricing negotiations, complaints, complex requests) route to Telegram where the owner makes the final call. This builds trust and catches edge cases the AI misses.
