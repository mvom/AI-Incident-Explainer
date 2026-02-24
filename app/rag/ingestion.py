import os
import json
import numpy as np
from pathlib import Path
from openai import OpenAI
from pinecone import Pinecone
from dotenv import load_dotenv
from tqdm import tqdm

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# -----------------------------
# Initialize OpenAI client and Pinecone
# -----------------------------
client = OpenAI(api_key=OPENAI_API_KEY)
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

# -----------------------------
# Dataset path
# -----------------------------
DATA_PATH = Path("data/raw/industrial_incidents.json")

# -----------------------------
# Utility functions
# -----------------------------
def incident_to_text(incident: dict) -> str:
    return f"""
Incident ID: {incident['incident_id']}
Timestamp: {incident['timestamp']}
Equipment: {incident['equipment']} ({incident['equipment_type']})
Location: {incident['location']}
Severity: {incident['severity']}
Error Type: {incident['error_type']}
Root Cause: {incident['root_cause']}
Resolution: {incident['resolution']}
Downtime: {incident['downtime_minutes']} minutes
"""

def generate_embeddings(texts):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )
    return [record.embedding for record in response.data]

# -----------------------------
# Batch ingestion to Pinecone
# -----------------------------
BATCH_SIZE = 50

# Load the dataset
with open(DATA_PATH, "r") as f:
    incidents = json.load(f)

print(f"Total incidents to ingest: {len(incidents)}")

# Use tqdm for a progress bar
for i in tqdm(range(0, len(incidents), BATCH_SIZE), desc="Ingesting batches"):
    batch = incidents[i:i+BATCH_SIZE]
    texts = [incident_to_text(inc) for inc in batch]
    embeddings = generate_embeddings(texts)

    to_upsert = [
        (inc["incident_id"], emb, {"error_type": inc["error_type"], "equipment": inc["equipment"]})
        for inc, emb in zip(batch, embeddings)
    ]

    index.upsert(vectors=to_upsert)

print("✅ Ingestion completed successfully!")