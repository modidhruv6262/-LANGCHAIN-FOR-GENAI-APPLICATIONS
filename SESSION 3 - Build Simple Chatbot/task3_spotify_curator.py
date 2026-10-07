import os
import warnings
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

warnings.filterwarnings('ignore')
load_dotenv()

llm = ChatGroq(model_name="openai/gpt-oss-20b", temperature=0.8)

prompt = PromptTemplate(
    input_variables=["genre"],
    template="Suggest a great {genre} song in the style of an energetic Spotify playlist curator."
)

chain = prompt | llm

print("--- Spotify Curator Bot ---")
genre = input("What genre of music do you want a recommendation for? ")

response = chain.invoke({"genre": genre})
print("\nCurator:", response.content)
