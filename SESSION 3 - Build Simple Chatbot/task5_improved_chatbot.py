import warnings
from dotenv import load_dotenv
from langchain_groq import ChatGroq

warnings.filterwarnings('ignore')
load_dotenv()

llm = ChatGroq(model_name="openai/gpt-oss-20b", temperature=0.7)

chat_history = [
    {"role": "system", "content": "You are a hyper-enthusiastic IPL superfan! You MUST include fun emojis in every response and hype up the user's favorite team."}
]

print("--- Improved IPL Chatbot (Type 'exit' to quit) ---")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        break

    chat_history.append({"role": "user", "content": user_input})

    response = llm.invoke(chat_history)

    print("Bot:", response.content)
    chat_history.append({"role": "assistant", "content": response.content})
