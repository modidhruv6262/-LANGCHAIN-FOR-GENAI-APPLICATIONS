import warnings
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import Tool

warnings.filterwarnings('ignore')
load_dotenv()

def custom_calculator(expression: str) -> str:
    try:
        allowed = "0123456789+-*/(). "
        if any(c not in allowed for c in expression):
            return "Invalid characters"
        return str(eval(expression))
    except Exception as e:
        return str(e)

calc_tool = Tool(
    name="Calculator",
    func=custom_calculator,
    description="Useful for evaluating math expressions."
)

agent = create_agent(
    model="groq:openai/gpt-oss-20b",
    tools=[calc_tool],
    system_prompt="You are a helpful assistant. Use the Calculator tool to answer math queries."
)

print("--- Calculator Agent ---")
user_query = "What is 15*3?"
print("User:", user_query)

response = agent.invoke({"messages": [{"role": "user", "content": user_query}]})
print("Agent:", response['messages'][-1].content)
