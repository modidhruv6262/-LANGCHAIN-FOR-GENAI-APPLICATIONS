### 4. How RAG Improves Chatbot Answers

Retrieval-Augmented Generation (RAG) significantly improves the quality of answers compared to a plain language model because it grounds the LLM's responses in factual, external data. 

A plain LLM might confidently hallucinate a restaurant recommendation or rely on generic, outdated training data. By using RAG, the chatbot first retrieves the exact, hyper-relevant reviews or facts from our specific local vector database (Chroma), and then passes that exact context to the LLM. This ensures the chatbot always answers using the most accurate, real-world data we provided it.
