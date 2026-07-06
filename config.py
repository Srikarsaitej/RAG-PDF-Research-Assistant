# LLM Configuration
LLM_MODEL = "llama3.2"

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Text Splitter
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval
TOP_K = 3

# Chroma Database
CHROMA_DB_DIR = "./chroma_db"

# App Information
APP_NAME = "AI PDF Research Assistant"

APP_DESCRIPTION = """
Chat intelligently with your PDF documents using
Retrieval-Augmented Generation (RAG),
LangChain, ChromaDB and Llama 3.2.
"""