import warnings
from dotenv import load_dotenv
from langchain_groq import ChatGroq

warnings.filterwarnings('ignore')
load_dotenv()

llm = ChatGroq(model_name="openai/gpt-oss-20b", temperature=0.7)

chat_history = []

print("--- 2-Message Memory Chatbot (Type 'exit' to quit) ---")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        break

    chat_history.append({"role": "user", "content": user_input})

    if len(chat_history) > 2:
        chat_history = chat_history[-2:]

    response = llm.invoke(chat_history)

    print("Bot:", response.content)
    chat_history.append({"role": "assistant", "content": response.content})
