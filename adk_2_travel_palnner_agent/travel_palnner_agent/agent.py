"""AI assistant to help users to search and summarise news and plan the trips using hotels and flights booking."""

from google.adk.agents import LlmAgent
from travel_palnner_agent.sub_agents.news_agent import news_agent   
from travel_palnner_agent.sub_agents.trip_planner_agent import trip_planner_agent


root_agent = LlmAgent(
    name="ai_assistant",
    model="gemini-2.0-flash",
    description=(
        "Agent to help users to search and summarise news and plan the trips using hotels and flights booking."
    ),
    instruction=(
        """
        You are multipurpose agent that can help users to search and summarise news and plan the trips using 
        hotels and flights booking.
        Use the sub-agents to accomplish the tasks.
        Be polite and concise in your responses. Ask clarifying questions if needed.
        """
    ),
    sub_agents=[trip_planner_agent, news_agent],
)
