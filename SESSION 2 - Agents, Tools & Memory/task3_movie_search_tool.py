import warnings
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool

warnings.filterwarnings('ignore')
load_dotenv()

@tool
def search_trending_movies(platform: str) -> str:
    """Search for the latest trending movies on a given platform like BookMyShow."""
    mock_movies = {
        "bookmyshow": ["Kalki 2898 AD", "Munjya", "Chandu Champion", "Inside Out 2"],
        "netflix": ["Hit Man", "Under Paris", "Bridgerton Season 3"]
    }
    platform = platform.lower().replace(" ", "")
    movies = mock_movies.get(platform)
    if movies:
        return f"Trending on {platform}: " + ", ".join(movies)
    return f"No trending data found for platform: {platform}"

agent = create_agent(
    model="groq:openai/gpt-oss-20b",
    tools=[search_trending_movies],
    system_prompt="You are an entertainment assistant. Use the search_trending_movies tool to fetch movie lists."
)

print("--- Testing Movie Search Agent ---")
response = agent.invoke({"messages": [{"role": "user", "content": "Show me trending movies on BookMyShow"}]})
print("\nFinal Answer:", response['messages'][-1].content)
