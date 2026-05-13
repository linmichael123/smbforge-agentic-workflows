# How I Built & Deployed This

**From scratch to production in 4 weeks — solo, $0 fixed-cost infra.**

1. **Conversational prototype → multi-agent system** — started with a single LLM prompt that handled SMS conversations. Iterated through 5+ major architecture revisions as real customers hit edge cases. Broke it into specialized agents (SMS, voice, escalation) with an orchestrator routing between them.

2. **Picked the cheapest stack that could scale** — Cloudflare Workers + D1 (SQLite) + KV. Everything runs on the $0 free tier. Telnyx for SMS/voice at ~$50/mo. Google Calendar/Sheets APIs for scheduling/invoicing. No VMs, no containers, no monthly bills to worry about.

3. **Built the owner interface in Telegram** — 27 tool declarations, all LLM-native. No custom dashboard to build or maintain. The owner approves bookings, manages campaigns, and monitors escalations from a single Telegram chat.

4. **Deployed with determinism** — Cloudflare Workers deployed via Wrangler CLI. macOS LaunchAgents schedule outreach and maintenance tasks. All secrets in Workers secrets (not env files). Production demo line live at **(949) 565-1908** on day one.

**Stack:** TypeScript + Hono · Cloudflare Workers/D1/KV · Telnyx · Gemini 2.5 Flash · Telegram Bot API · Google Calendar/Sheets · Stripe
