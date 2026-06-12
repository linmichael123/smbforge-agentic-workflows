# AI Invoicing — Example API Calls

Test the invoicing agent locally with curl:

```bash
# Create an invoice
curl -X POST http://localhost:8787/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Create an invoice for Jane Smith (jane@example.com) for $125.00 — plumbing repair labor.",
    "senderId": "demo_session_2"
  }'

# Check invoice status (after webhook fires)
curl -X POST http://localhost:8787/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Has the invoice for Jane been paid?",
    "senderId": "demo_session_2"
  }'
```

Expected response:

```json
{
  "reply": "Here's the payment link for Jane's plumbing repair: https://checkout.stripe.com/c/pay/cs_test_...",
  "status": "active"
}
```
