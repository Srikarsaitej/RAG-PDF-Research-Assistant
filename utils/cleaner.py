import re


def clean_documents(documents):
    """
    Cleans PDF text before chunking.
    """

    cleaned_docs = []

    for doc in documents:

        text = doc.page_content

        # Remove multiple spaces
        text = re.sub(r"\s+", " ", text)

        # Remove page numbers like "Page 1"
        text = re.sub(r"Page\s+\d+", "", text, flags=re.IGNORECASE)

        # Remove repeated blank lines
        text = re.sub(r"\n+", "\n", text)

        doc.page_content = text.strip()

        cleaned_docs.append(doc)

    return cleaned_docs