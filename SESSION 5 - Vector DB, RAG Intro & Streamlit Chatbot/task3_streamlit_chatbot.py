import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

st.title("Food Recommendation RAG Bot")

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="restaurant_reviews")
model = SentenceTransformer('all-MiniLM-L6-v2')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask for a food recommendation...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    query_embedding = model.encode([user_input]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=1)
    best_review = results['documents'][0][0]

    bot_response = f"Based on our database, here is the most relevant review: '{best_review}'"

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
