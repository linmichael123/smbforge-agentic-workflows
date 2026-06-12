# AI Ordering Agent — Architecture & API Patterns

Standalone conversational product catalog & cart manager on Cloudflare Workers.

## Architecture

```
POST /chat  →  LLM (Gemini/OpenAI)  →  Tool: browse_catalog
                                    →  Tool: add_to_cart
                                    →  Tool: remove_from_cart
                                    →  Tool: view_cart
```

## Tool Definitions

### `browse_catalog`
- **What it does:** Shows available products/services from a JSON catalog
- **Parameters:** category filter (optional)
- **Returns:** Formatted product list with prices

### `add_to_cart`
- **What it does:** Adds an item to the customer's cart in KV
- **Parameters:** product_id, quantity
- **Returns:** Updated cart summary

### `remove_from_cart`
- **What it does:** Removes or reduces quantity of a cart item
- **Parameters:** product_id, quantity
- **Returns:** Updated cart summary

### `view_cart`
- **What it does:** Shows current cart contents and total
- **Returns:** Line items + total price

## Catalog Schema

```typescript
interface Product {
  id: string;
  name: string;
  description: string;
  price: number;        // in dollars (e.g. 18.00)
  category: string;
  available: boolean;
}

// Example catalog — customize this array
const CATALOG: Product[] = [
  { id: "prod_1", name: "Premium Coffee Beans", description: "Single-origin, medium roast", price: 18.00, category: "coffee", available: true },
  { id: "prod_2", name: "Espresso Blend", description: "Dark roast, Italian-style", price: 22.00, category: "coffee", available: true },
  { id: "prod_3", name: "Consultation Session", description: "30-min video consultation", price: 75.00, category: "services", available: true },
];
```

## Cart State Pattern

```typescript
// Stored in KV per session
interface CartState {
  sessionId: string;
  items: Array<{ productId: string; name: string; unitPrice: number; quantity: number }>;
  total: number;
  lastUpdated: string;  // ISO timestamp
}
```

---

👉 **[Get the full deployable template on Gumroad →](https://michaelforge0.gumroad.com/l/bmsorr)**  
Includes: complete TypeScript source, catalog schema, KV cart persistence, README with customization guide.
