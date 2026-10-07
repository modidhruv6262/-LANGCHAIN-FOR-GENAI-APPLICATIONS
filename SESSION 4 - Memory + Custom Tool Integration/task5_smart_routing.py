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
    description="Evaluates math expressions."
)

routing_prompt = (
    "You are a highly intelligent assistant. "
    "If the user asks a mathematical calculation, you MUST use the Calculator tool. "
    "If the user asks a general question (like 'Hello' or 'How are you?'), answer normally without using the tool."
)

agent = create_agent(
    model="groq:openai/gpt-oss-20b",
    tools=[calc_tool],
    system_prompt=routing_prompt
)

print("--- Smart Routing Agent ---")

q1 = "Hi, how are you?"
print("\nUser:", q1)
response1 = agent.invoke({"messages": [{"role": "user", "content": q1}]})
print("Agent:", response1['messages'][-1].content)

q2 = "What is 452 divided by 4?"
print("\nUser:", q2)
response2 = agent.invoke({"messages": [{"role": "user", "content": q2}]})
print("Agent:", response2['messages'][-1].content)
