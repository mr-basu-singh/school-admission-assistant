from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader
)

import os


def load_documents():

    documents = []

    pdf_folder = "data/pdfs"
    doc_folder = "data/docs"
    txt_folder = "data/txt"

    # PDFs
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_folder, file))
            documents.extend(loader.load())

    # DOCX
    for file in os.listdir(doc_folder):
        if file.endswith(".docx"):
            loader = Docx2txtLoader(os.path.join(doc_folder, file))
            documents.extend(loader.load())

    # TXT
    for file in os.listdir(txt_folder):
        if file.endswith(".txt"):
            loader = TextLoader(
                os.path.join(txt_folder, file),
                encoding="utf-8"
            )
            documents.extend(loader.load())

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print("=" * 60)

    print(f"Total Documents Loaded : {len(docs)}")

    print("=" * 60)

    for i, doc in enumerate(docs):

        print(f"\nDocument {i+1}")

        print(doc.metadata)

        print(doc.page_content[:200])