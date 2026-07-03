from rag.splitter import split_documents
from rag.embedding import embeddings

from langchain_chroma import Chroma


def create_vector_store():

    chunks = split_documents()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    print("=" * 60)
    print("Vector Database Created Successfully!")
    print("=" * 60)

    return vectorstore


if __name__ == "__main__":
    create_vector_store()