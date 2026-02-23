### 🤖 Marketing AI Agent: RFM Segmentation via MCP 📊
## Project Overview
This project bridges the gap between Machine Learning and Creative Strategy. I developed a custom Model Context Protocol (MCP) server in Python that allows an AI Agent to query live customer segmentation data directly from a local environment.

By giving the AI access to real metrics (Recency and Frequency), I eliminated "segmentation hallucination" and ensured that every marketing campaign drafted is mathematically grounded in actual customer behavior.

## Key Features
1) Data-Driven Logic: Uses a Python-based segmentation model (VIPs, Loyalists, Occasional) to drive outreach strategy.

2) FastMCP Infrastructure: Built a dedicated server that exposes a get_cluster_insights tool to the AI.

3) Agentic Workflow: The agent autonomously identifies the need for data, executes the Python tool, and interprets the results.

4) Efficiency Gain: Achieved a 30%+ reduction in campaign drafting time by automating the data-verification step.

When asked to optimize a campaign for "Occasional" customers, the agent:

1) Queried the MCP server.

2) Identified that "Loyalists" average 40 orders.

3) Calculated the specific "delta" (2 more orders) needed to move the segment up.

4) Generated high-conversion subject lines like: "Order 2x this month unlock Loyalist perks + 25% off".

## Tech Stack
1) Language: Python (Pandas)

2) Framework: FastMCP

3) Environment: VS Code & GitHub Copilot

## Future Roadmap: Azure Cloud Deployment for global accessibility.
