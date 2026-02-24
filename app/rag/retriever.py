# app/rag/retriever.py
from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

def query_incidents(vector, top_k=5):
    """
    Retrieve top_k most similar incidents from Pinecone using a query vector.
    """
    results = index.query(vector=vector, top_k=top_k, include_metadata=True)
    return results