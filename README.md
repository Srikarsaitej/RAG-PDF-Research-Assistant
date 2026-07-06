# 📄 AI PDF Research Assistant (RAG)

An AI-powered **Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents and interact with them using natural language. The application leverages **Llama 3.2**, **LangChain**, **HuggingFace Embeddings**, and **ChromaDB** to provide context-aware, document-grounded responses through a clean Streamlit interface.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- 💬 Ask natural language questions about uploaded PDFs
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Local LLM inference using **Llama 3.2 (Ollama)**
- 🔍 Semantic search using HuggingFace embeddings
- 💾 ChromaDB vector database for efficient retrieval
- 📚 Context-aware document question answering
- 📊 Displays document metadata (pages & chunks)
- 💡 Suggested questions for quick interaction
- 🎨 Clean and interactive Streamlit UI
- 💬 Persistent chat history during the session

---

# 🏗️ System Architecture

```
                PDF Document
                     │
                     ▼
            PyPDF Document Loader
                     │
                     ▼
         Recursive Text Splitter
                     │
                     ▼
       HuggingFace Embeddings
                     │
                     ▼
              Chroma Vector DB
                     │
                     ▼
          Top-K Relevant Chunks
                     │
                     ▼
            LangChain RAG Pipeline
                     │
                     ▼
          Llama 3.2 (Ollama Local)
                     │
                     ▼
              Final AI Response
```

---

# 📸 Application Screenshots

## 🏠 Home Page

![Home](screenshots/home.png)

---

## 📂 Upload PDF

![Upload](screenshots/upload.png)

---

## 💬 Chat Interface

![Chat](screenshots/chat.png)

---

# ⚙️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | RAG Orchestration |
| Ollama | Local LLM Runtime |
| Llama 3.2 | Large Language Model |
| HuggingFace | Sentence Embeddings |
| ChromaDB | Vector Database |
| PyPDF | PDF Loading |
| RecursiveCharacterTextSplitter | Document Chunking |

---

# 📂 Project Structure

```
AI-PDF-Chatbot/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│
├── data/
│   └── sample.pdf
│
├── screenshots/
│   ├── home.png
│   ├── upload.png
│   └── chat.png
│
├── styles/
│   └── style.css
│
└── utils/
    ├── pdf_loader.py
    ├── splitter.py
    ├── embeddings.py
    ├── vector_store.py
    └── rag_pipeline.py
```

---

# 🔄 Workflow

1. Upload a PDF document.
2. Extract text using **PyPDFLoader**.
3. Split the document into overlapping chunks.
4. Generate semantic embeddings using **all-MiniLM-L6-v2**.
5. Store embeddings in **ChromaDB**.
6. Retrieve the most relevant chunks for a user query.
7. Pass the retrieved context to **Llama 3.2** through LangChain.
8. Generate a context-aware response.

---

# 🧠 RAG Pipeline

```
User Question
      │
      ▼
Semantic Search
      │
      ▼
Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Llama 3.2
      │
      ▼
Generated Answer
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/AI-PDF-Chatbot.git

cd AI-PDF-Chatbot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download from:

https://ollama.com

Pull the model:

```bash
ollama pull llama3.2
```

Run Ollama:

```bash
ollama serve
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 💡 Example Questions

- Summarize this document.
- Explain the methodology.
- What technologies are used?
- List the key findings.
- Who are the authors?
- What problem does this paper solve?
- Explain the architecture.
- Give me the conclusion.

---

# 📈 Future Improvements

- Multiple PDF support
- Conversation memory
- PDF highlighting
- Citation-based responses
- Chat export (PDF/Markdown)
- Authentication
- Cloud deployment
- Docker support
- Multi-user support

---

# 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Prompt Engineering
- LangChain
- Large Language Models
- Streamlit Development
- Local LLM Deployment
- Python Application Development

---

# 👨‍💻 Author

**Srikar Sai Tej**

GitHub:
https://github.com/<YOUR_GITHUB_USERNAME>

LinkedIn:
<YOUR_LINKEDIN_URL>

---

# ⭐ If you found this project useful, consider giving it a Star!