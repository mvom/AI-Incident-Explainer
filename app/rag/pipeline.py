from app.rag.embeddings import embed_query, client
from app.rag.retriever import query_incidents


def answer_question(question, top_k=3):
    query_vec = embed_query(question)
    results = query_incidents(query_vec, top_k=top_k)
    context = "\n".join([f"Incident {r['id']}: {r['metadata']}" for r in results['matches']])
    prompt = f"""
You are an AI assistant for industrial incidents.
Use the following incidents as context to answer the question.
Context:
{context}

Question: {question}
Answer:"""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content