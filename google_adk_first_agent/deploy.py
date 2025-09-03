"""Deploy the agent to Vertex AI Agent Engine."""

import os
from dotenv import load_dotenv

import vertexai
from vertexai.preview.reasoning_engines import AdkApp

from google_search_agent.agent import root_agent

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    staging_bucket=os.getenv("STAGING_BUCKET"),
)

app = AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

remote_app = vertexai.agent_engines.create(
    app,
    display_name="google_search_agent",
    requirements=[
        "google-cloud-aiplatform[adk,agent-engines]>=1.100.0,<2.0.0",
        "google-adk>=1.5.0,<2.0.0"
    ],
    extra_packages=[
        "./google_search_agent",
    ],
)

print(f"Deployed agent successfully, resource name: {remote_app.resource_name}")
