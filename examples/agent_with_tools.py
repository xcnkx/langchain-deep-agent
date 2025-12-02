"""Agent with tools/function calling example.

This example demonstrates how to create an agent that can use tools (functions)
to perform specific tasks.
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Ensure API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found in environment variables. Please set it in .env file."
    )


# Define tools using the @tool decorator
@tool
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


@tool
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


@tool
def get_weather(location: str) -> str:
    """Get the weather for a location (mock function).

    Args:
        location: The city name

    Returns:
        Weather information
    """
    # This is a mock function. In a real application, you would call a weather API
    return f"The weather in {location} is sunny with a temperature of 22°C."


def main():
    """Run an agent with tools."""
    # Initialize the LLM with tools
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Bind tools to the model
    tools = [calculate_sum, calculate_product, get_weather]
    llm_with_tools = llm.bind_tools(tools)

    # Example 1: Simple calculation
    print("Example 1: Simple calculation")
    print("-" * 50)
    messages = [
        SystemMessage(content="You are a helpful assistant that can use tools."),
        HumanMessage(content="What is 15 plus 27?"),
    ]

    response = llm_with_tools.invoke(messages)
    print(f"Response: {response}")

    # Check if the model wants to call a tool
    if hasattr(response, "tool_calls") and response.tool_calls:
        print(f"\nTool called: {response.tool_calls[0]['name']}")
        print(f"Arguments: {response.tool_calls[0]['args']}")

        # Execute the tool
        if response.tool_calls[0]["name"] == "calculate_sum":
            args = response.tool_calls[0]["args"]
            result = calculate_sum.invoke(args)
            print(f"Result: {result}")

    print("\n" + "=" * 50 + "\n")

    # Example 2: Weather query
    print("Example 2: Weather query")
    print("-" * 50)
    messages = [
        SystemMessage(content="You are a helpful assistant that can use tools."),
        HumanMessage(content="What's the weather like in Tokyo?"),
    ]

    response = llm_with_tools.invoke(messages)
    print(f"Response: {response}")

    # Check if the model wants to call a tool
    if hasattr(response, "tool_calls") and response.tool_calls:
        print(f"\nTool called: {response.tool_calls[0]['name']}")
        print(f"Arguments: {response.tool_calls[0]['args']}")

        # Execute the tool
        if response.tool_calls[0]["name"] == "get_weather":
            args = response.tool_calls[0]["args"]
            result = get_weather.invoke(args)
            print(f"Result: {result}")


if __name__ == "__main__":
    main()
