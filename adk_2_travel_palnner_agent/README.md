# AI Assistant (Multi-Agent System)

This tutorial contains multi-agent system built using google adk. It contains AI assistant which is able to:

- Summarise the latest news using SerpAPI
- Plan trips using google flights and hotels data using serpAPI

---

## Prerequisites

- Python installed
- A **GCP Project** with:
  - **Billing enabled**
  - **Vertex AI APIs** enabled
- [gcloud CLI](https://cloud.google.com/sdk/docs/install) configured
- SerpAPI account and its API key

---

## Run the Agent Locally

### 1. Clone the Repository
```bash
git clone <repo_url>
cd <repo_name>/adk_2_travel_palnner_agent/
```

### 2. Setup Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Google ADK

```bash
python -m pip install -r requirements.txt
```

### 5. Setup env file

Copy env file and update the provided variables.

```bash
cp .env.example .env
```

### 6. Run Agent Locally

- Via web UI. Access via the provided local URL.
```bash
adk web
```


## Reference URLs

- ADK official documentation: https://google.github.io/adk-docs/agents/multi-agents/
- Sample Agents: https://github.com/google/adk-samples
