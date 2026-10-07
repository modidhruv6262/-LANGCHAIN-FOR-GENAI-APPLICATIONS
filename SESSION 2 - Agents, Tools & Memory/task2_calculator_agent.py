import warnings
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool

warnings.filterwarnings('ignore')
load_dotenv()

@tool
def calculator_tool(expression: str) -> str:
    """Evaluate a mathematical expression. Input should be a mathematical string like '12 * 8'."""
    try:
        allowed_chars = "0123456789+-*/(). "
        if any(c not in allowed_chars for c in expression):
            return "Error: Invalid characters in math expression."
        return str(eval(expression))
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

agent = create_agent(
    model="groq:openai/gpt-oss-20b",
    tools=[calculator_tool],
    system_prompt="You are a math assistant. You MUST use the calculator_tool to solve ANY math problem."
)

print("--- Testing Calculator Agent ---")
response = agent.invoke({"messages": [{"role": "user", "content": "What is 12 times 8?"}]})
print("\nFinal Answer:", response['messages'][-1].content)
