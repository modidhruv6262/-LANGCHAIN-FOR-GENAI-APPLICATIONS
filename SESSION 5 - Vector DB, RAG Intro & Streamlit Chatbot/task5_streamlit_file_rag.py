import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

st.title("Food Facts RAG Bot")

client = chromadb.PersistentClient(path="./food_facts_db")
collection = client.get_or_create_collection(name="food_facts")
model = SentenceTransformer('all-MiniLM-L6-v2')

if collection.count() == 0:
    with open("food_facts.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    embeddings = model.encode(lines).tolist()
    collection.add(
        documents=lines,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(lines))]
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask a question about food facts...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    query_embedding = model.encode([user_input]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=1)
    best_fact = results['documents'][0][0]

    bot_response = f"I found this fact for you: {best_fact}"

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
