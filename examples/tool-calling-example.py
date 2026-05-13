#!/usr/bin/env python3
"""
Tool-Calling Example: Booking Agent

Safe, abstracted pseudocode showing how the SMS Conversation Agent
uses tool-calling with an LLM to handle appointment booking.

This is NOT production code. It demonstrates the architecture pattern.
"""

import json
from typing import TypedDict, Optional
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

class Message(TypedDict):
    role: str          # "user" | "assistant" | "system" | "tool"
    content: str
    timestamp: str

class ToolCall(TypedDict):
    name: str
    arguments: dict

class ToolResult(TypedDict):
    name: str
    result: dict

class Conversation(TypedDict):
    id: int
    tenant_id: str
    messages: list[Message]
    status: str        # "active" | "resolved" | "escalated"

# ---------------------------------------------------------------------------
# Tool Implementations (simplified)
# ---------------------------------------------------------------------------

class GoogleCalendarTool:
    """Maps to the actual Google Calendar API calls."""
    
    def check_availability(self, duration_minutes: int = 30) -> list[str]:
        """
        Check Google Calendar for free slots in the next 3 business days.
        
        In production: calls Google Calendar API freebusy query,
        filters out booked slots, returns formatted time blocks.
        """
        # Simulated — in production this hits the Google Calendar API
        now = datetime.now()
        slots = []
        for day_offset in range(1, 4):
            date = now + timedelta(days=day_offset)
            if date.weekday() < 5:  # Mon-Fri
                for hour in [9, 10, 11, 13, 14, 15, 16]:
                    slots.append(f"{date.strftime('%a %b %d')} at {hour}:00")
        return slots

    def book_appointment(self, name: str, phone: str, time_slot: str) -> dict:
        """
        Book appointment into Google Calendar.
        
        In production: creates a Google Calendar event via API,
        adds customer details to description, sends confirmation.
        """
        return {
            "success": True,
            "event_id": "evt_abc123",
            "time": time_slot,
            "confirmation": f"Confirmed: {time_slot} for {name}",
        }


class EscalationTool:
    """Handles escalation to the business owner via Telegram."""
    
    def escalate_to_owner(self, conversation_id: int, reason: str) -> dict:
        """
        Escalate conversation to business owner.
        
        In production: sends Telegram message with conversation context,
        updates D1 conversation status to 'escalated', logs the flag.
        """
        return {
            "success": True,
            "notified": True,
            "message": f"Owner notified — reason: {reason}",
        }


class OrderTool:
    """Handles plan ordering and invoicing."""
    
    def parse_order(self, plan_name: str) -> dict:
        """
        Extract structured order from natural language.
        
        In production: calls LLM to extract plan name from customer message,
        validates against product catalog, returns order structure.
        """
        return {
            "success": True,
            "plan": plan_name,
            "monthly": 99.00,
            "setup": 199.00,
            "features": [
                "AI scheduling",
                "Google Calendar sync",
                "AI ordering & invoicing",
                "Google Sheets tracker",
            ],
        }


# ---------------------------------------------------------------------------
# LLM Integration (Agent Loop)
# ---------------------------------------------------------------------------

class LLMService:
    """Abstracted LLM service — wraps any provider (Gemini, Claude, etc.)."""
    
    def generate(
        self,
        system_prompt: str,
        messages: list[Message],
        tools: list[dict]
    ) -> tuple[str, Optional[ToolCall]]:
        """
        Call the LLM with system prompt, message history, and available tools.
        
        Returns: (response_text, tool_call_if_made)
        
        In production: calls Gemini API with function declarations,
        parses the function_call response, routes to tool execution.
        """
        raise NotImplementedError("Replace with actual LLM API call")


def run_conversation_loop(llm: LLMService, conversation: Conversation, tools: dict) -> None:
    """
    Main agent conversation loop.
    
    Each customer message triggers:
    1. Build system prompt with client context
    2. Call LLM with message history + tool declarations
    3. If LLM requests a tool call → execute tool → feed result back
    4. If LLM responds with text → send to customer
    5. Repeat until: resolved, escalated, or MAX_ROUNDS reached
    
    This loop is capped at MAX_ROUNDS=3 to prevent infinite tool loops.
    """
    MAX_ROUNDS = 3
    
    system_prompt = build_system_prompt(conversation["tenant_id"])
    messages = conversation["messages"]
    
    for round_num in range(MAX_ROUNDS):
        # Step 1: Call LLM
        response_text, tool_call = llm.generate(
            system_prompt=system_prompt,
            messages=messages,
            tools=list(tools.keys()),
        )
        
        # Step 2: Route to tool or respond
        if tool_call:
            if tool_call["name"] in tools:
                result = tools[tool_call["name"]](**tool_call["arguments"])
                messages.append({
                    "role": "tool",
                    "content": json.dumps(result),
                    "timestamp": datetime.now().isoformat(),
                })
                # Loop back — let LLM process the tool result
                continue
        else:
            # Step 3: Send text response to customer
            send_sms(conversation["customer_phone"], response_text)
            messages.append({
                "role": "assistant",
                "content": response_text,
                "timestamp": datetime.now().isoformat(),
            })
            break
    
    # Persist updated conversation
    save_conversation(conversation["id"], messages)


def build_system_prompt(tenant_id: str) -> str:
    """
    Assemble the system prompt from:
    - Client skill file (KV: skill:client:{tenant_id})
    - Routing rules
    - Escalation triggers
    - Conversation limits
    - Current date/time (for calendar queries)
    
    The final prompt is 800-1200 tokens depending on client complexity.
    """
    client_skill = load_client_skill(tenant_id)
    return f"""
You are the AI assistant for {client_skill['business_name']}.

## Business Context
{json.dumps(client_skill, indent=2)}

## Today's Date
{datetime.now().strftime('%A, %B %d, %Y')}

## Rules
[Rules extracted from client skill — greeting, booking flow, escalation]

## Available Tools
- check_availability: Check calendar for free slots
- book_appointment: Book into Google Calendar
- escalate_to_owner: Transfer to human owner
- parse_order: Parse a plan order
- submit_order: Submit order for approval

## Escalation Triggers (MANDATORY)
[Triggers extracted from client skill — emergencies, pricing, complaints]
"""


# ---------------------------------------------------------------------------
# Placeholder helpers (not implemented in this example)
# ---------------------------------------------------------------------------

def send_sms(phone: str, message: str) -> None:
    """Send SMS via Telnyx API."""
    pass

def save_conversation(conv_id: int, messages: list[Message]) -> None:
    """Persist conversation to D1."""
    pass

def load_client_skill(tenant_id: str) -> dict:
    """Load client configuration from KV."""
    return {"business_name": "Example Plumbing", "hours": "Mon-Fri 9-5"}


# ---------------------------------------------------------------------------
# Usage Example
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """
    This module demonstrates the agent loop architecture.
    
    To run in production:
    1. Instantiate LLMService with your provider + key
    2. Set up tool implementations with real API keys
    3. Call run_conversation_loop() per incoming message
    
    The entire agent system fits in this ~200-line pattern:
    - System prompt assembly → LLM call → Tool execution → Response
    - MAX_ROUNDS prevents infinite loops
    - Escalation triggers catch edge cases
    - D1 persistence provides audit trail
    """
    print("Tool-calling architecture demonstrated above.")
    print("See architecture/agent-architecture.md for the full system.")
