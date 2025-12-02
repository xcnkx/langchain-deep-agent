"""Basic LangChain agent example.

This example demonstrates how to create a simple LangChain agent that can
answer questions using OpenAI's GPT models.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables from .env file
load_dotenv()

# Ensure API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in .env file.")


def main():
    """Run a basic agent conversation."""
    # Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
    )
    
    # Create messages
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="What is LangChain and why is it useful?"),
    ]
    
    # Get response
    response = llm.invoke(messages)
    
    print("AI Response:")
    print(response.content)


if __name__ == "__main__":
    main()
