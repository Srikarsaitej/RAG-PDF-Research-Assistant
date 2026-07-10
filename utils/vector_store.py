from langchain_chroma import Chroma


def create_vector_store(chunks, embedding_model):
    """
    Creates an in-memory Chroma vector database.
    A new database is created for each uploaded PDF.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store