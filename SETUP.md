# How These Templates Were Born

Built from a live production system that handles real customer scheduling, invoicing, and ordering for service businesses.

## The Origin

I spent 4 weeks building a production multi-agent AI system for service businesses (plumbers, electricians, cleaners). It took real calls and SMS conversations, booked appointments on Google Calendar, generated Stripe invoices, and handled escalations — all autonomously.

After running it in production, I extracted the core agent modules into standalone, self-hosted templates. No proprietary plumbing, no multi-tenant infrastructure — just clean, focused agents that do one thing well.

## Why I'm Selling Templates Instead of SaaS

I tried the SaaS route. Cold email: 0% reply rate after 492 sends. Cold SMS: low pickup. The lesson: **service business owners don't buy software from strangers on the internet.**

But developers, agencies, and technical founders? They buy proven boilerplates that save them weeks of building. And they don't want another $50/mo subscription — they want code they own.

## What Makes These Different

Every template uses:

- **Zero SDKs** — Google Calendar and Stripe are called via raw `fetch()`. No `npm install googleapis` fiasco on Workers.
- **$0/mo hosting** — Runs on Cloudflare free tier.
- **Dual LLM support** — Gemini 1.5 Flash ($0.07/1M tokens) or OpenAI. Toggle with one env var.
- **Unified `/chat` API** — One endpoint, any channel (SMS, WhatsApp, Telegram, web widget).

## Architecture Patterns

Each template follows the same clean pattern:

```
worker/
├── src/
│   ├── index.ts           # Hono entrypoint (chat route)
│   ├── env.ts             # TypeScript env definitions (no real secrets)
│   ├── orchestrator.ts    # LLM tool-calling loop
│   ├── database/
│   │   └── db.ts          # Persistence adapter (KV or memory)
│   └── shared/
│       ├── llm.ts         # Gemini/OpenAI gateway
│       └── [service].ts   # REST client (gcal.ts, stripe.ts)
├── wrangler.toml
├── package.json
└── README.md              # Full setup guide with OAuth walkthrough
```

## The Pivot

After 492 cold emails with 0 replies and a $500 Google Ads credit burning at $15+ CPC, I realized: you can't sell to tradespeople through the same channels everyone else uses.

So I'm selling to the people who *build for* tradespeople — agencies, dev shops, and technical founders who need a proven conversational AI backend they can deploy, customize, and resell.

The SaaS is on hold. The templates are live.
