# AI Invoicing Agent — Architecture & API Patterns

Standalone conversational invoicing agent using Stripe REST API on Cloudflare Workers.

## Architecture

```
POST /chat           →  LLM (Gemini/OpenAI)  →  Tool: create_invoice
                                               →  Stripe REST API

POST /webhook/stripe  →  Stripe event handler  →  checkout.session.completed
                                               →  Confirmation SMS
```

## Tool Definitions

### `create_invoice`
- **What it does:** Creates a Stripe Price, then a Payment Link, returns the checkout URL
- **API used:** `POST https://api.stripe.com/v1/prices` + `POST https://api.stripe.com/v1/payment_links`
- **Parameters:** line_items (name, quantity, unit_price), customer email
- **Returns:** Stripe checkout URL + payment status

## Key Pattern: SDK-Free Stripe

```typescript
async function createPrice(secretKey: string, amount: number, currency: string): Promise<string> {
  const resp = await fetch("https://api.stripe.com/v1/prices", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${secretKey}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      currency,
      "unit_amount": String(Math.round(amount * 100)),
      "product_data[name]": "Service Invoice",
    }),
  });
  const data = await resp.json<{ id: string }>();
  return data.id;
}
```

Same pattern as Google Calendar — no `stripe` npm package. Works on Workers with zero issues.

## Webhook Pattern

The `/webhook/stripe` endpoint:
1. Receives `checkout.session.completed` event from Stripe
2. Verifies the webhook signature using `STRIPE_WEBHOOK_SECRET`
3. Looks up the conversation session from KV
4. Sends confirmation message to the customer

## Conversation State

Maintained in Cloudflare KV:

```typescript
interface InvoiceState {
  sessionId: string;
  status: "collecting_items" | "awaiting_payment" | "paid" | "cancelled";
  lineItems: Array<{ name: string; quantity: number; unitPrice: number }>;
  paymentUrl?: string;
}
```

---

👉 **[Get the full deployable template on Gumroad →](https://michaelforge0.gumroad.com/l/oqmbqe)**  
Includes: complete TypeScript source, webhook handler, wrangler.toml, Stripe setup guide.
