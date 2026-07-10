import streamlit as st

from utils.pdf_loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store
from utils.rag_pipeline import create_rag_chain

from utils.router import is_summary_request
from utils.summarizer import summarize_document

from utils.document_insights import generate_document_insights

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI PDF Research Assistant",
    page_icon="📄",
    layout="wide"
)


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    try:
        with open("styles/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )
    except:
        pass


load_css()

# ==========================================================
# SESSION STATE
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "pdf_loaded" not in st.session_state:
    st.session_state.pdf_loaded = False

if "file_name" not in st.session_state:
    st.session_state.file_name = ""

if "pages" not in st.session_state:
    st.session_state.pages = 0

if "chunk_count" not in st.session_state:
    st.session_state.chunk_count = 0

if "document_chunks" not in st.session_state:
    st.session_state.document_chunks = []

if "document_insights" not in st.session_state:
    st.session_state.document_insights = ""



# ==========================================================
# TITLE
# ==========================================================

st.markdown("""
# 📄 AI PDF Research Assistant

### Chat with your documents using **Retrieval-Augmented Generation (RAG)**

Built with **LangChain • HuggingFace • ChromaDB • Ollama • Llama 3.2**
""")

if st.session_state.pdf_loaded:

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📄 Pages", st.session_state.pages)

    c2.metric("✂ Chunks", st.session_state.chunk_count)

    c3.metric("🤖 Model", "Llama3.2")

    c4.metric("🧠 Embedding", "MiniLM")


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type="pdf"
    )

    # ======================================================
    # PROCESS PDF
    # ======================================================

    if uploaded_file and not st.session_state.pdf_loaded:

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        progress = st.progress(0)

        status = st.empty()

        status.info("📄 Reading PDF...")

        progress.progress(10)

        documents = load_pdf("temp.pdf")

        from utils.cleaner import clean_documents

        documents = clean_documents(documents)

        status.info("✂ Splitting document...")

        progress.progress(30)

        chunks = split_documents(documents)

        # Store chunks for summarization
        st.session_state.document_chunks = chunks

        # Store chunk count for sidebar
        st.session_state.chunk_count = len(chunks)

        status.info("🧠 Loading embedding model...")

        progress.progress(50)

        embedding_model = get_embedding_model()

        status.info("💾 Creating vector database...")

        progress.progress(70)

        vector_store = create_vector_store(
            chunks,
            embedding_model
        )

        status.info("🔍 Building retriever...")

        progress.progress(90)

        retriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 6,
                "fetch_k": 20
            }
        )

        st.session_state.rag_chain = create_rag_chain(
            retriever
        )

        st.session_state.document_insights = generate_document_insights(chunks)

        progress.progress(100)

        status.success("✅ PDF Ready!")

        st.session_state.file_name = uploaded_file.name
        st.session_state.pages = len(documents)
        st.session_state.chunk_count = len(chunks)
        st.session_state.pdf_loaded = True

    # ======================================================
    # SIDEBAR DASHBOARD
    # ======================================================

    if st.session_state.pdf_loaded:

        st.divider()

        st.markdown(f"""
<div class="card">

<h3>📄 Document</h3>

<b>{st.session_state.file_name}</b>

<br><br>

📑 Pages : <b>{st.session_state.pages}</b>

<br>

✂ Chunks : <b>{st.session_state.chunk_count}</b>

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="card">

<h3>🤖 AI Engine</h3>

LLM : <b>Llama 3.2</b>

<br>

Embedding : <b>MiniLM-L6-v2</b>

<br>

Retriever : <b>Top-3 Similar Chunks</b>

<br>

Database : <b>ChromaDB</b>

<br><br>

<span style="color:green;"><b>🟢 Ready</b></span>

</div>
""", unsafe_allow_html=True)
        
        if st.session_state.document_insights:

            st.divider()

            st.subheader("📄 AI Insights")

            st.info(st.session_state.document_insights)

        st.divider()

        st.markdown("### 💡 Suggested Questions")

        summary_btn = st.button("📄 Summarize Document")

        objective_btn = st.button("🎯 Objective")

        methodology_btn = st.button("🧠 Methodology")

        technology_btn = st.button("💻 Technologies")

        st.divider()

    else:

        summary_btn = False
        objective_btn = False
        methodology_btn = False
        technology_btn = False

    # ======================================================
    # CLEAR CHAT
    # ======================================================

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.session_state.rag_chain = None
        st.session_state.pdf_loaded = False
        st.session_state.file_name = ""
        st.session_state.pages = 0
        st.session_state.chunks = 0

        st.rerun()

# ==========================================================
# CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ==========================================================
# CHAT INPUT
# ==========================================================

question = None

if st.session_state.pdf_loaded:

    # Suggested Questions

    if summary_btn:
        question = "Summarize this document."

    elif objective_btn:
        question = "What is the objective of this document?"

    elif methodology_btn:
        question = "Explain the methodology used in this document."

    elif technology_btn:
        question = "What technologies are used in this document?"

    # User Input

    user_input = st.chat_input(
        "Ask anything about your PDF..."
    )

    if user_input:
        question = user_input


# ==========================================================
# CHAT EXECUTION
# ==========================================================

if question:

    # -----------------------------
    # User Message
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # -----------------------------
    # Assistant Message
    # -----------------------------

    with st.chat_message("assistant"):

        placeholder = st.empty()

        with st.spinner("Thinking..."):

            if is_summary_request(question):

                answer = summarize_document(
                    st.session_state.document_chunks
                )

                response = None

            else:

                response = st.session_state.rag_chain.invoke(
                {
                    "input": question
                }
            )

                answer = response["answer"]



        # Simple typing effect

        displayed = ""

        for word in answer.split():

            displayed += word + " "

            placeholder.markdown(displayed + "▌")

        placeholder.markdown(answer)

        # -----------------------------
        # Source Pages
        # -----------------------------

        if response is not None and "context" in response:

            st.markdown("### 📄 Sources")

            pages = sorted(
                set(
                    doc.metadata.get("page", 0) + 1
                    for doc in response["context"]
                )
            )

            st.write(", ".join([f"Page {p}" for p in pages]))

            if pages:

                st.divider()

                st.caption("📄 Source Pages")

                cols = st.columns(len(pages))

                for i, page in enumerate(pages):
                    cols[i].success(f"Page {page}")

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


# ==========================================================
# HOME SCREEN
# ==========================================================

if not st.session_state.pdf_loaded:

    st.markdown("---")

    st.markdown("""
# 👋 Welcome

Upload a PDF from the sidebar and start asking questions.

### What you can do

- 📄 Summarize documents
- 🔍 Search information
- 📚 Explain concepts
- 🧠 Extract insights
- 💡 Answer questions
- 📊 Analyze reports

---

### Technologies Used

- LangChain
- ChromaDB
- HuggingFace
- Ollama
- Llama 3.2
- Streamlit

---
""")


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center; color:gray; font-size:14px;">

Built with ❤️ by <b>Srikar Sai Tej</b>

<br><br>

Python • Streamlit • LangChain • ChromaDB • HuggingFace • Ollama

</div>
""",
unsafe_allow_html=True
)