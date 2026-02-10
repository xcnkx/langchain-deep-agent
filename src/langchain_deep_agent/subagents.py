from langchain_deep_agent.tools import internet_search

def get_research_subagent() -> dict:
    return {
        "name": "research-agent",
        "description": "Used to research more in depth questions",
        "system_prompt": "You are a great researcher",
        "tools": [internet_search],
        "model": "openai:gpt-5.2",  # Optional override, defaults to main agent model
    }