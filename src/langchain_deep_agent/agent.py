from deepagents import create_deep_agent
from langchain_deep_agent.tools import internet_search
from langchain_deep_agent.subagents import get_research_subagent
from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
from langgraph.store.memory import InMemoryStore
from langgraph.checkpoint.memory import MemorySaver
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


def get_deep_agent_with_subagent():
    subagents = [get_research_subagent()]

    agent =  create_deep_agent(
        model=model,
        subagents=subagents
    )
    return agent

def get_deep_agent_with_memory():
    checkpointer = MemorySaver()

    def make_backend(runtime):
        return CompositeBackend(
            default=StateBackend(runtime),  # Ephemeral storage
            routes={
                "/memories/": StoreBackend(runtime)  # Persistent storage
            }
        )

    agent = create_deep_agent(
        store=InMemoryStore(),  # Required for StoreBackend
        backend=make_backend,
        checkpointer=checkpointer
    )

    return agent


if __name__ == "__main__":
    agent = get_research_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": "TAVIのCT計測の問題点を教えて?"}]})

    # Print the agent's response
    print(result["messages"][-1].content)