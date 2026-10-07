import warnings
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool

warnings.filterwarnings('ignore')
load_dotenv()

@tool
def food_delivery_search(restaurant: str) -> str:
    """Search for a restaurant's menu prices."""
    menu = {
        "mcdonalds": {"burger": 150, "fries": 100},
        "dominos": {"pizza": 350, "coke": 50}
    }
    res = menu.get(restaurant.lower())
    if res:
        return str(res)
    return "Restaurant not found."

@tool
def calculator_tool(expression: str) -> str:
    """Evaluate a mathematical expression. Input should be a math string like '150 + 100'."""
    try:
        allowed_chars = "0123456789+-*/(). "
        if any(c not in allowed_chars for c in expression):
            return "Error: Invalid characters."
        return str(eval(expression))
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

agent = create_agent(
    model="groq:openai/gpt-oss-20b",
    tools=[food_delivery_search, calculator_tool],
    system_prompt="You are a smart food delivery assistant. You can look up menu prices and calculate the total bill for the user."
)

print("--- Testing Combined Agent (Food Domain) ---")
print("User: How much would it cost to order a pizza and two cokes from Dominos?")
response = agent.invoke({"messages": [{"role": "user", "content": "How much would it cost to order a pizza and two cokes from Dominos?"}]})

# Safe print to avoid Windows cp1252 crash since user requested no sys.stdout hack
output = response['messages'][-1].content
print("\nFinal Answer:", output)
