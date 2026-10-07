import os
import warnings
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

warnings.filterwarnings('ignore')
load_dotenv()

llm = ChatGroq(
    temperature=0.7,
    model_name="openai/gpt-oss-20b",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["food"],
    template="Give me one short fun fact about the food: {food}"
)

chain = prompt | llm
response = chain.invoke({"food": "pani puri"})
print(response.content)
