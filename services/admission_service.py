import sqlite3

from rag.retriever import get_retriever
from llm.gemini import ask_gemini


retriever = get_retriever()


def query_database(question):

    conn = sqlite3.connect("database/school.db")

    cursor = conn.cursor()

    q = question.lower()

    data = ""

    if "fee" in q:

        cursor.execute("SELECT * FROM fees")

        data = cursor.fetchall()

    elif "seat" in q:

        cursor.execute("SELECT * FROM seats")

        data = cursor.fetchall()

    elif "transport" in q:

        cursor.execute("SELECT * FROM transport")

        data = cursor.fetchall()

    elif "visit" in q:

        cursor.execute("SELECT * FROM campus_visit")

        data = cursor.fetchall()

    conn.close()

    return str(data)


def ask_school_assistant(question):

    docs = retriever.invoke(question)

    document_context = ""

    sources = []

    for doc in docs:

        document_context += doc.page_content + "\n\n"

        sources.append(doc.metadata["source"])

    database_context = query_database(question)

    prompt = f"""

You are an AI Admission Assistant.

Answer ONLY using the information below.

-------------------------

DOCUMENTS

{document_context}

-------------------------

DATABASE

{database_context}

-------------------------

Question

{question}

Answer clearly.

At the end provide the sources used.

"""

    answer = ask_gemini(prompt)

    return {
    "answer": answer,
    "sources": list(set(sources))}


if __name__ == "__main__":

    question = input("Ask : ")

    print()

    print(ask_school_assistant(question))