import warnings
from dotenv import load_dotenv
from langchain_groq import ChatGroq

warnings.filterwarnings('ignore')
load_dotenv()

llm = ChatGroq(model_name="openai/gpt-oss-20b", temperature=0.7)

print("--- Welcome to the IPL Chatbot! ---")
team = input("Enter your favorite IPL team: ")

messages = [
    {"role": "system", "content": "You are a friendly cricket fan. Give a short, enthusiastic response about the user's favorite IPL team."},
    {"role": "user", "content": f"My favorite team is {team}"}
]

response = llm.invoke(messages)
print("\nChatbot:", response.content)
