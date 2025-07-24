from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

server_params = StdioServerParameters(
    command = r"D:\AIVIS_MCP\.venv\Scripts\python.exe",
    args = [r"server\weather.py"]
)

async def main(input):
    
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model,tools)
            agent_response = await agent.ainvoke({"messages":input})
            return agent_response
        
if __name__ == "__main__":
    input = "What is the current weather at Delhi?"
    result = asyncio.run(main(input))
    print(result['messages'][-1].content)
