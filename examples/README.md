# Examples README

This directory contains example scripts demonstrating various LangChain features and patterns.

## Available Examples

### 1. basic_agent.py
A simple example showing how to create a basic LangChain agent that can answer questions using OpenAI's GPT models.

**Run:**
```bash
uv run examples/basic_agent.py
```

### 2. chat_agent.py
An interactive chat agent with conversation history management. This example shows how to maintain context across multiple turns of conversation.

**Run:**
```bash
uv run examples/chat_agent.py
```

**Commands:**
- Type your message to chat with the agent
- Type `reset` to clear conversation history
- Type `quit` to exit

### 3. agent_with_tools.py
Demonstrates how to create an agent with tools (function calling). The agent can use custom functions to perform specific tasks like calculations or fetching information.

**Run:**
```bash
uv run examples/agent_with_tools.py
```

## Prerequisites

Before running any examples, make sure you have:
1. Set up your environment (see main README.md)
2. Created a `.env` file with your OpenAI API key
3. Installed all dependencies using `uv sync`

## Customization

Feel free to modify these examples to experiment with different:
- Models (gpt-3.5-turbo, gpt-4, etc.)
- Temperature settings
- System prompts
- Tools and functions
- Message structures
