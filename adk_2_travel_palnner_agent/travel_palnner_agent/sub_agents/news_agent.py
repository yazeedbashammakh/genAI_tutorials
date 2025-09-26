"""Flight search agent"""

from google.adk.agents import LlmAgent

from travel_palnner_agent.tools.news import search_news


AGENT_INSTRUCTIONS = """
You are a News Summariser Assistant. 
Your task is to find news about given topics or events and provide concise summaries.
Show output in well structured and easy-to-read markdown format.
"""


news_agent = LlmAgent(
    name="news_agent",
    model="gemini-2.0-flash",
    description=(
        """
        News Agent to search and summarise news about given topics or events.
        If user asks anything apart from news then delegate to parent agent agent.
        """
    ),
    instruction=AGENT_INSTRUCTIONS,
    tools=[search_news],
)
