# AI Scheduler — Example API Calls

Test the scheduling agent locally with curl:

```bash
# List available slots
curl -X POST http://localhost:8787/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What slots do you have available tomorrow afternoon?",
    "senderId": "demo_session_1"
  }'

# Book an appointment
curl -X POST http://localhost:8787/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Book me for tomorrow at 2 PM. My name is Alex.",
    "senderId": "demo_session_1"
  }'

# Cancel
curl -X POST http://localhost:8787/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Cancel my appointment please.",
    "senderId": "demo_session_1"
  }'
```

Expected response format:

```json
{
  "reply": "I've checked the calendar. Tomorrow at 2:00 PM is available!",
  "status": "active"
}
```
