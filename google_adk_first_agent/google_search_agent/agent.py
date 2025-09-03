"""Agent definition for Google Search Agent."""

from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="google_search_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions using Google Search."
    ),
    instruction=(
        """
        You are a helpful AI assistant that uses Google Search to find information.
        Be polite and concise in your responses. Ask clarifying questions if needed.
        """
    ),
    tools=[google_search],
)
