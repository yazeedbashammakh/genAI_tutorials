"""Flight search agent"""

import os
from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from dotenv import load_dotenv

from .flight_tools import search_flights

load_dotenv()

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "true")
os.environ["GOOGLE_CLOUD_PROJECT"] = os.getenv("GOOGLE_CLOUD_PROJECT")
os.environ["GOOGLE_CLOUD_LOCATION"] = os.getenv("GOOGLE_CLOUD_LOCATION")


AGENT_INSTRUCTIONS = """
You are a Flights Search Agent.
Your task is to search for flights based on the given query and return the best possible results. 
Always provide results in structured JSON format with the following fields:

- airline_name
- flight_number
- departure_airport
- arrival_airport
- departure_time
- arrival_time
- duration
- price
- booking_link (if available)

Add more fields if necessary.

Guidelines:
- Suggest minimum 3 options sorted based on user preference (e.g., price, duration).
- Make sure times and prices are clear and human-readable.
- Do not add extra commentary; return only the flight information.
- If input is missing details (like dates), ask clarifying questions.
"""


root_agent = LlmAgent(
    name="flights_agent",
    model="gemini-2.0-flash",
    description=(
        "Flights Search Agent"
    ),
    instruction=AGENT_INSTRUCTIONS,
    tools=[search_flights],
)


a2a_app = to_a2a(root_agent, port=8001)
