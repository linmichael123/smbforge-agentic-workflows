# SMB Forge: Self-Hosted Conversational AI Agent Templates

**3 production-grade Cloudflare Workers templates** — scheduling, invoicing, and ordering AI agents you can deploy in 5 minutes for **$0/mo** (free tier).

No SaaS subscriptions. No vendor lock-in. Just TypeScript, Hono, and zero-dependency REST integrations.

---

## ⬇️ Quick Download

Want the source as a deploy-ready ZIP? Grab the latest release:
**[SMB Forge v0.1.0 →](https://github.com/linmichael123/smbforge-agentic-workflows/releases/latest)**

Each ZIP includes LICENSE, README, and all source — `unzip` → `npm install` → `wrangler deploy`.

---

## 🗓️ AI Scheduler — $29

Google Calendar conversational booking agent. Handles `list_free_slots`, `book_appointment`, `cancel_appointment` via LLM tool calls.

- **Stack:** Hono + Cloudflare Workers + Google Calendar REST API
- **LLM:** Gemini 1.5 Flash or OpenAI GPT-4o-mini (toggle with one env var)
- **Storage:** Cloudflare KV or local memory
- **Channel:** Single `/chat` endpoint → works with SMS, WhatsApp, Telegram, web widgets

[📦 Get the full deployable template on Gumroad →](https://michaelforge0.gumroad.com/l/sitqsv)

See [products/ai-scheduler/](products/ai-scheduler/) for the architecture and API patterns.

---

## 💳 AI Invoicing — $29

Stripe conversational invoicing agent. Compiles line items, generates checkout links, handles webhook confirmations — all in the chat.

- **Stack:** Hono + Cloudflare Workers + Stripe REST API (SDK-free)
- **Webhook:** Pre-wired `/webhook/stripe` for `checkout.session.completed`
- **LLM:** Same dual-engine support (Gemini/OpenAI/any OpenAI-compatible)
- **Storage:** Cloudflare KV or local memory

[📦 Get the full deployable template on Gumroad →](https://michaelforge0.gumroad.com/l/oqmbqe)

See [products/ai-invoicing/](products/ai-invoicing/) for the architecture and API patterns.

---

## 🛍️ AI Ordering — $19

Conversational product catalog & cart manager. Guides customers through selection, tracks quantities, calculates totals.

- **Stack:** Hono + Cloudflare Workers
- **Catalog:** Simple JSON array — customize instantly
- **Cart:** Stateful KV persistence across turns
- **LLM:** Same dual-engine support

[📦 Get the full deployable template on Gumroad →](https://michaelforge0.gumroad.com/l/bmsorr)

See [products/ai-ordering/](products/ai-ordering/) for the architecture and API patterns.

---

## 🏢 Master Bundle — $79

All 3 agents unified under a single orchestrator. The AI can browse products, book appointments, and generate invoices in one conversation.

[📦 Get the Master Bundle on Gumroad →](https://michaelforge0.gumroad.com/l/amlwjk)

---

## Why These Templates?

**No SDKs.** Google Calendar and Stripe integrations use raw `fetch()` — zero dependency incompatibilities with Cloudflare Workers. Deployable in 5 minutes, not 5 hours.

**No monthly fees.** Self-hosted on Cloudflare's free tier. Pay only for your LLM API usage ($0.07/1M tokens for Gemini Flash).

**No lock-in.** Full TypeScript source. MIT licensed. Extend for any niche — plumbers, HVAC, dental clinics, SaaS onboarding.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Runtime | Cloudflare Workers (TypeScript, Hono) |
| Storage | Cloudflare KV (or local memory for dev) |
| LLM | Gemini 1.5 Flash / OpenAI GPT-4o-mini / any OpenAI-compatible |
| Scheduling | Google Calendar REST API (no SDK) |
| Payments | Stripe REST API (no SDK) |
| Chat API | Single `/chat` endpoint → SMS, WhatsApp, web widgets |

---

## About SMB Forge

We build conversational AI systems for service businesses. After running a live production system handling real customer scheduling, invoicing, and ordering, we extracted these battle-tested modules into standalone templates.

Built by **Michael Lin** — [GitHub](https://github.com/linmichael123) · michael@smbforge.com

---

*Each template is MIT licensed and includes a complete README with OAuth walkthroughs, LLM cost optimization guide, and production deployment instructions.*
