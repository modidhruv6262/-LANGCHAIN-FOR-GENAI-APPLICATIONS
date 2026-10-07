import os
import warnings
from dotenv import load_dotenv
from langchain.agents import create_agent

warnings.filterwarnings('ignore')
load_dotenv()

agent = create_agent(
    model="groq:openai/gpt-oss-20b",
    system_prompt="You are a friendly conversational assistant."
)

print("--- Testing Conversational Memory Agent ---")

# Memory handled using a minimal list and roles
chat_history = []

print("User: Hi, my name is Dhruv.")
chat_history.append({"role": "user", "content": "Hi, my name is Dhruv."})
response1 = agent.invoke({"messages": chat_history})
chat_history = response1['messages']
print("Agent:", chat_history[-1].content, "\n")

print("User: What is my name?")
chat_history.append({"role": "user", "content": "What is my name?"})
response2 = agent.invoke({"messages": chat_history})
chat_history = response2['messages']
print("Agent:", chat_history[-1].content)
