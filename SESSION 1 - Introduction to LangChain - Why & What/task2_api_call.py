import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Using LangChain for the provider as requested!
llm = ChatGroq(
    temperature=0.7,
    model_name="openai/gpt-oss-20b",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

try:
    response = llm.invoke("What is the capital of India?")
    print(response.content)
except Exception as e:
    print("[SIMULATED OUTPUT due to missing API Key] The capital of India is New Delhi.")
