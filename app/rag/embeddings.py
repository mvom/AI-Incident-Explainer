from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def embed_query(query_text):
    """
    Create embedding vector for a user query using OpenAI.
    """
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=query_text
    )
    return resp.data[0].embedding