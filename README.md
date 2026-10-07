<div align="center">
  
# 🦜🔗 LangChain for GenAI Applications

![LangChain](https://img.shields.io/badge/LangChain-1.4.3-blue?style=for-the-badge&logo=chainlink)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-orange?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-API-green?style=for-the-badge)

*A comprehensive exploration of LangChain, AI Agents, Memory Management, and Retrieval-Augmented Generation (RAG).*

</div>

---

## 📖 Overview

This repository contains five modular, fully functional projects demonstrating the power of **LangChain** for building next-generation AI applications. It transitions smoothly from basic LLM API calls to advanced, fully autonomous tool-calling Agents and Streamlit-powered RAG chatbots.

Every session is cleanly separated into its own directory with dedicated virtual environments to prevent dependency conflicts, adhering to strict minimalist coding practices (zero unnecessary comments, streamlined logic).

---

## 🗂️ Project Structure & Features

### 🌟 Session 1: Introduction to LangChain
**Folder:** `SESSION 1 - Introduction to LangChain - Why & What`
- Basic direct-to-LLM API interactions.
- Building dynamic `PromptTemplate` objects.
- Creating native LangChain Chains to process text sequences efficiently.

### 🤖 Session 2: Agents, Tools & Memory
**Folder:** `SESSION 2 - Agents, Tools & Memory`
- Implementation of modern `create_agent` graph frameworks.
- Building robust python-based `@tool` functions (e.g., mathematical calculators).
- Intelligent agents capable of executing search tools for dynamic data fetching (IPL Captains & Movie Searches).

### 💬 Session 3: Build Simple Chatbot
**Folder:** `SESSION 3 - Build Simple Chatbot`
- Interactive command-line chatbot architectures.
- Dynamic persona swapping (e.g., "Spotify Playlist Curator" or "Enthusiastic IPL Superfan").
- Continuous conversational looping handling dynamic follow-ups natively.

### 🧠 Session 4: Memory + Custom Tool Integration
**Folder:** `SESSION 4 - Memory + Custom Tool Integration`
- Advanced memory management bypassing bloated classes for hyper-minimalist list-based State Graphs.
- Implementation of the native LangChain `Tool` class objects.
- "Smart Routing" — creating prompt architectures that teach the LLM exactly when to invoke an internal tool vs when to answer conversationally.

### 🚀 Session 5: Vector DB, RAG & Streamlit
**Folder:** `SESSION 5 - Vector DB, RAG Intro & Streamlit Chatbot`
- **Retrieval-Augmented Generation (RAG):** Eliminating hallucinations by grounding LLMs in external text files.
- **Vector Databases:** Setting up localized `ChromaDB` instances for semantic searching.
- **Embeddings:** Utilizing `sentence-transformers` (`all-MiniLM-L6-v2`) to embed text mathematically.
- **Web UIs:** Deploying responsive chat interfaces directly into the browser using `Streamlit`.

---

## 🛠️ Installation & Usage

Every session operates completely independently. To run a specific session, navigate into its folder, activate its isolated environment, and run the scripts!

### 1. Set Up Your API Key
All sessions use the **Groq API** for ultra-fast Llama inferencing. 
Create a `.env` file in the root of the session you want to run:
```env
GROQ_API_KEY="your_groq_api_key_here"
```

### 2. Activate & Run (Sessions 1-4)
```powershell
# Navigate into the session folder
cd "SESSION 2 - Agents, Tools & Memory"

# Activate the virtual environment
.\env\Scripts\activate

# Run any python task script natively
python task1_ipl_agent.py
```

### 3. Running Streamlit Web Apps (Session 5)
```powershell
# Navigate into Session 5
cd "SESSION 5 - Vector DB, RAG Intro & Streamlit Chatbot"

# Activate environment
.\env\Scripts\activate

# Launch the Web UI!
streamlit run task3_streamlit_chatbot.py
```

---

## 💡 Key Takeaways
- **Modularity:** Demonstrated by strictly decoupling tool functions from agent logic.
- **State Management:** Mastered by maintaining exact N-message sliding window histories.
- **RAG Architecture:** Showcased by seamlessly combining SentenceTransformers, ChromaDB, and Groq LLMs to chat directly with local datasets.

<div align="center">
  <br>
  <i>Built with ❤️ using LangChain, Groq, and Python.</i>
</div>
