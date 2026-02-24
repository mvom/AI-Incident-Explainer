from app.rag.pipeline import answer_question

if __name__ == "__main__":
    question = input("Ask a question about incidents: ")
    response = answer_question(question)
    print("\nAI Response:\n")
    print(response)