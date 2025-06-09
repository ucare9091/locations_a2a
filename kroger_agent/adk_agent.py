
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

def create_agent() -> LlmAgent:
    """Constructs the ADK agent."""
    return LlmAgent(
        model="gemini-2.5-flash-preview-04-17",
        name="kroger_agent",
        description="An agent that can help questions about kroger store locations",
        instruction=f"""You are a specialized kroger store location assistant. Your primary function is to utilize the provided tools to retrieve and relay kroger store location information in response to user queries. You must rely exclusively on these tools for data and refrain from inventing information. Ensure that all responses include the detailed output from the tools used and are formatted in Markdown""",
        tools=[
            MCPToolset(
                connection_params=StdioServerParameters(
                    command="python",
                    args=["./kroger_server.py"],
                ),
            )
        ],
    )
