from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.loader import load_documents


def split_documents():

    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":

    chunks = split_documents()

    print("=" * 60)
    print(f"Total Chunks : {len(chunks)}")
    print("=" * 60)

    for i, chunk in enumerate(chunks[:5]):

        print(f"\nChunk {i+1}")
        print(chunk.metadata)
        print(chunk.page_content[:250])