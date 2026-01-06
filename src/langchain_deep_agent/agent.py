from deepagents import create_deep_agent
from .tools import internet_search

from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-5.2")

# System prompt to steer the agent to be an expert researcher
def get_research_agent():
    research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

    You should use JAPANESE language for your responses and reports.

    You have access to an internet search tool as your primary means of gathering information.

    ## `internet_search`

    Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
    """
    agent = create_deep_agent(
            model=model,
            tools=[internet_search],
            system_prompt=research_instructions
        )
    return agent


if __name__ == "__main__":
    agent = get_research_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

    # Print the agent's response
    print(result["messages"][-1].content)