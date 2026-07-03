from langchain_chroma import Chroma

from rag.embedding import embeddings


def get_retriever():

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    query = "What documents are required for admission?"

    docs = retriever.invoke(query)

    print("=" * 70)

    print("Retrieved Documents")

    print("=" * 70)

    for i, doc in enumerate(docs, start=1):

        print(f"\nResult {i}")

        print(doc.metadata)

        print("-" * 40)

        print(doc.page_content)