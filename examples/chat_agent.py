"""Interactive chat agent example.

This example demonstrates how to create an interactive chat agent with
conversation history management.
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Ensure API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY not found in environment variables. Please set it in .env file."
    )


class ChatAgent:
    """A simple chat agent that maintains conversation history."""

    def __init__(self, model: str = "gpt-3.5-turbo", temperature: float = 0.7):
        """Initialize the chat agent.

        Args:
            model: The OpenAI model to use
            temperature: The temperature for response generation
        """
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.messages = [
            SystemMessage(content="You are a helpful AI assistant. Be friendly and concise.")
        ]

    def chat(self, user_message: str) -> str:
        """Send a message and get a response.

        Args:
            user_message: The user's message

        Returns:
            The AI's response
        """
        # Add user message to history
        self.messages.append(HumanMessage(content=user_message))

        # Get AI response
        response = self.llm.invoke(self.messages)

        # Add AI response to history
        self.messages.append(AIMessage(content=response.content))

        return response.content

    def reset(self):
        """Reset the conversation history."""
        self.messages = [
            SystemMessage(content="You are a helpful AI assistant. Be friendly and concise.")
        ]


def main():
    """Run an interactive chat session."""
    agent = ChatAgent()

    print("Chat Agent Started! (type 'quit' to exit, 'reset' to clear history)")
    print("-" * 50)

    while True:
        # Get user input
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if user_input.lower() == "reset":
            agent.reset()
            print("Conversation history cleared!")
            continue

        # Get and print response
        response = agent.chat(user_input)
        print(f"\nAI: {response}")


if __name__ == "__main__":
    main()
