from langchain_ollama import ChatOllama


def generate_document_insights(chunks):
    """
    Generates AI insights about the uploaded document.
    """

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    text = ""

    # Read the first few chunks
    for chunk in chunks[:6]:
        text += chunk.page_content + "\n\n"

    prompt = f"""
Analyze the following document and provide:

Title:
Document Type:
Domain:
Difficulty:
Estimated Reading Time:
Top 5 Keywords:

Document:

{text}
"""

    response = llm.invoke(prompt)

    return response.content