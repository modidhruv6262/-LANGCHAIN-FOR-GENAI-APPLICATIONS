import chromadb
from sentence_transformers import SentenceTransformer

def search_similar_review(query):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="restaurant_reviews")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=1
    )

    return results['documents'][0][0]

query = "best pizza"
best_match = search_similar_review(query)

print(f"Query: {query}")
print(f"Most similar review: {best_match}")
