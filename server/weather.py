from mcp.server.fastmcp import FastMCP

mcp = FastMCP("current weather")

@mcp.tool(name="weather_fetch", description="Fetches weather info for a given location")
def weather_fetch(location:str) -> str:
    weather_info = "Weather data for {}: Sunny, 25°C".format(location)
    return weather_info

if __name__ == "__main__":
    mcp.run(transport="stdio")