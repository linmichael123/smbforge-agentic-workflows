# AI Ordering — Example API Calls

Test the ordering agent locally with curl:

```bash
# Browse catalog
curl -X POST http://localhost:8787/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What products do you have?",
    "senderId": "demo_session_3"
  }'

# Add to cart
curl -X POST http://localhost:8787/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Add 2 bags of Premium Coffee Beans to my cart.",
    "senderId": "demo_session_3"
  }'

# View cart
curl -X POST http://localhost:8787/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What's in my cart?",
    "senderId": "demo_session_3"
  }'
```

Expected response:

```json
{
  "reply": "I've added 2x Premium Coffee Beans ($36.00 total) to your cart!",
  "status": "active",
  "cart": [
    { "id": "prod_1", "name": "Premium Coffee Beans", "price": 18, "quantity": 2 }
  ]
}
```
