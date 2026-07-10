from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=700,

        chunk_overlap=150,

        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            " ",
            ""
        ]
    )

    return splitter.split_documents(documents)