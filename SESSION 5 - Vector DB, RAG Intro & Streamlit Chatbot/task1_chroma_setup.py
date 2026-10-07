import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="restaurant_reviews")

reviews = [
    "The best pizza in town, the crust is perfectly crispy and cheesy.",
    "Terrible service, I waited an hour for my cold pasta.",
    "Amazing sushi, very fresh fish and great atmosphere.",
    "The burgers are extremely juicy and the fries are crunchy.",
    "Average food, nothing special about their tacos."
]

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(reviews).tolist()

collection.add(
    documents=reviews,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(reviews))]
)

print("5 restaurant reviews successfully stored in Chroma DB.")
