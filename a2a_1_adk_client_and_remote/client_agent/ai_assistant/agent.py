"""AI assistant to help users to search and summarise news and plan the trips using hotels and flights booking."""

from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent



flights_agent = RemoteA2aAgent(
    name="flights_agent",
    description="Agent to search flights",
    agent_card=(
        f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

hotels_agent = RemoteA2aAgent(
    name="hotels_agent",
    description="Agent to search hotels.",
    agent_card=(
        f"http://localhost:8002/a2a/hotels_agent{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

root_agent = LlmAgent(
    name="ai_assistant",
    model="gemini-2.0-flash",
    description=(
        "Agent to help users to search flights and hotels. And plan the trips for users"
    ),
    instruction=(
        """
        You are multipurpose agent that can help users to search hotels and flights.
        Use the sub-agents to accomplish the tasks.
        Be polite and concise in your responses. Ask clarifying questions if needed.
        """
    ),
    sub_agents=[flights_agent, hotels_agent],
)
