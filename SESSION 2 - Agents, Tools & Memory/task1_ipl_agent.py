import os
import warnings
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool

warnings.filterwarnings('ignore')
load_dotenv()

@tool
def get_ipl_captain(team_name: str) -> str:
    """Get the captain of a specific IPL cricket team."""
    captains = {
        "gujarat titans": "Shubman Gill",
        "chennai super kings": "Ruturaj Gaikwad",
        "mumbai indians": "Hardik Pandya",
        "royal challengers bengaluru": "Faf du Plessis"
    }
    return captains.get(team_name.lower(), "Team not found in the predefined list.")

agent = create_agent(
    model="groq:openai/gpt-oss-20b",
    tools=[get_ipl_captain],
    system_prompt="You are a helpful IPL cricket assistant. Use the provided tools to answer questions."
)

print("--- Testing IPL Agent ---")
response = agent.invoke({"messages": [{"role": "user", "content": "Who is the captain of Gujarat Titans?"}]})
print("\nFinal Answer:", response['messages'][-1].content)
