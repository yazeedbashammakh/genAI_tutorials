"""Trip planner agent"""

from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool

from travel_palnner_agent.sub_agents.flights_agent import flights_agent
from travel_palnner_agent.sub_agents.hotels_agent import hotels_agent

# Convert specialized agents into AgentTools
flight_agent_tool = agent_tool.AgentTool(agent=flights_agent)
hotel_agent_tool = agent_tool.AgentTool(agent=hotels_agent)

AGENT_INSTRUCTIONS = """
You are a Trip Planning Agent. The user will describe their travel needs (origin, destination, dates, budget, preferences). 
Use flights_agent and hotels_agent to find the best flight and hotel options.
Finally, combine results in a user-friendly structured markdown format.

Guidelines:
- Do not hallucinate; rely on subagent outputs.
- Preserve clarity and consistency in date/time formats.
- If user input is incomplete, check if you can get it from subagents, or derive it logically, else ask clarifying questions.
- Prioritize user preferences (budget, amenities, etc.) when selecting options.
- If you encounter errors from subagents, handle them gracefully and inform the user.
- Use flight_agent for flight searches and hotel_agent for hotel searches.
- Show output in well structured and easy-to-read markdown format.
- If you cannot find suitable options, explain why and suggest alternatives.
- Always aim to provide the best possible travel plan for the user.
- Use google search tool if needed to find additional information.
- If user asks anything apart from trip planning then delegate to parent agent.
"""


trip_planner_agent = LlmAgent(
    name="trip_planner_agent",
    model="gemini-2.0-flash",
    description=(
        "Trip Planner Agent"
    ),
    instruction=AGENT_INSTRUCTIONS,
    tools=[flight_agent_tool, hotel_agent_tool],
)
