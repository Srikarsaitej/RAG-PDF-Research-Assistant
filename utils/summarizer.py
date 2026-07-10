from langchain_ollama import ChatOllama


def summarize_document(chunks):

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    text = ""

    for chunk in chunks[:15]:
        text += chunk.page_content + "\n\n"

    prompt = f"""
You are an AI Research Assistant.

Summarize the following technical document.

Your summary should include:

• Objective
• Problem Statement
• Proposed Solution
• Technologies Used
• Advantages
• Conclusion

Document:

{text}

Summary:
"""

    response = llm.invoke(prompt)

    return response.content