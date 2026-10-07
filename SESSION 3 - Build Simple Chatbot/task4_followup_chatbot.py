import warnings
from dotenv import load_dotenv
from langchain_groq import ChatGroq

warnings.filterwarnings('ignore')
load_dotenv()

llm = ChatGroq(model_name="openai/gpt-oss-20b", temperature=0.5)

chat_history = [
    {"role": "system", "content": "You are an IPL cricket expert. Answer questions concisely."}
]

print("--- IPL Interactive Chatbot (Type 'exit' to quit) ---")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        break

    chat_history.append({"role": "user", "content": user_input})

    response = llm.invoke(chat_history)

    print("Bot:", response.content)
    chat_history.append({"role": "assistant", "content": response.content})
