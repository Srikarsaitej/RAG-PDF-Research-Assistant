from langchain_ollama import ChatOllama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate


def create_rag_chain(retriever):

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template("""
    You are an AI Research Assistant specialized in analyzing technical documents.

    Answer the user's question ONLY using the provided context.

    Rules:

    • Be concise and factual.
    • If the answer spans multiple sections, combine the relevant information.
    • If the context contains partial information, answer with the available details instead of saying "I don't know."
    • Only reply "I couldn't find that information in the uploaded document." if none of the retrieved context is relevant.

    Context:
    {context}

    Question:
    {input}

    Answer:
    """)

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return retrieval_chain