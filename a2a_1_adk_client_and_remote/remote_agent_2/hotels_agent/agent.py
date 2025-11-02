"""Flight search agent"""

from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from .tools import search_hotels


AGENT_INSTRUCTIONS = """
You are a Hotels Recommendation Assistant. 
Your task is to find hotels based on the given destination, travel dates, and budget. 
Always return results in structured JSON format with the following fields:

- hotel_name
- location
- rating
- number_of_reviews
- amenities (list)
- price_per_night
- total_price (for stay duration)
- booking_link (if available)

Add more fields if necessary.

Guidelines:
- Suggest at least 3 hotels, sorted by user preference (e.g., price, rating, distance).
- Mention if free cancellation or breakfast is included.
- Do not include irrelevant commentary; only hotel details.
- If details like budget or dates are missing, ask clarifying questions.
"""


root_agent = LlmAgent(
    name="hotels_agent",
    model="gemini-2.0-flash",
    description=(
        "Hotel Search Agent"
    ),
    instruction=AGENT_INSTRUCTIONS,
    tools=[search_hotels],
)
