from mcp.server.fastmcp import FastMCP
import pandas as pd

# Initialize the MCP Server (The Bridge)
mcp = FastMCP("Segmentation_Agent")

@mcp.tool()
def get_cluster_insights():
    """Returns the average Recency and Frequency for each customer segment."""
    # This data mirrors your dashboard results
    data = {
        'Segment': ['VIPs', 'Loyalists', 'Occasional', 'At-Risk'],
        'Avg_Recency': [10, 30, 150, 250],
        'Avg_Frequency': [80, 40, 10, 2]
    }
    return pd.DataFrame(data).to_string()

if __name__ == "__main__":
    mcp.run()
    
    