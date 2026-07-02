"""Modern Streamlit frontend for the local RAG application.

This file reuses the existing backend modules from the src package without
modifying the backend logic.
"""

from datetime import datetime
from pathlib import Path

import streamlit as st

from src.config import Config
from src.embedding import create_embedding_model
from src.ingest import ingest_documents
from src.rag_chain import ask
from src.vector_store import load_vector_store

PROJECT_ROOT = Path(__file__).resolve().parent
INDEX_DIR = PROJECT_ROOT / "faiss_index"


def ensure_directories() -> None:
    """Create required folders for indexes."""
    INDEX_DIR.mkdir(parents=True, exist_ok=True)


def init_session_state() -> None:
    """Initialize Streamlit session state for chat history and folder selection."""
    st.session_state.setdefault("chat_history", [])
    st.session_state.setdefault("selected_folder", "")


def get_selected_folder() -> Path | None:
    """Return the currently selected folder as a Path object."""
    folder_value = st.session_state.get("selected_folder", "").strip()
    if not folder_value:
        return None
    return Path(folder_value).expanduser()


def get_pdf_files(folder_path: Path | None) -> list[Path]:
    """Return all PDF files under the selected folder."""
    if folder_path is None or not folder_path.exists() or not folder_path.is_dir():
        return []
    return sorted(path for path in folder_path.rglob("*.pdf") if path.is_file())


def get_chunk_count() -> int:
    """Return the number of indexed chunks if a vector store exists."""
    try:
        embedding_model = create_embedding_model()
        vector_store = load_vector_store(embedding_model)
        return int(getattr(getattr(vector_store, "index", None), "ntotal", 0) or 0)
    except Exception:
        return 0


def get_vector_store_summary() -> dict:
    """Collect summary information about the current vector database."""
    try:
        embedding_model = create_embedding_model()
        vector_store = load_vector_store(embedding_model)
        index = getattr(vector_store, "index", None)
        embedding_dimension = getattr(index, "d", None) or getattr(index, "dimension", None)
    except Exception:
        return {
            "embedding_model": Config.EMBEDDING_MODEL,
            "embedding_dimension": "Not built yet",
            "vector_db": "FAISS",
            "document_count": 0,
            "chunk_count": 0,
            "top_k": Config.TOP_K,
        }

    return {
        "embedding_model": Config.EMBEDDING_MODEL,
        "embedding_dimension": embedding_dimension or "Unknown",
        "vector_db": "FAISS",
        "document_count": len(get_pdf_files(get_selected_folder())),
        "chunk_count": int(getattr(index, "ntotal", 0) or 0),
        "top_k": Config.TOP_K,
    }


def render_dashboard() -> None:
    """Render the dashboard overview page."""
    st.header("🏠 Dashboard")
    st.caption("Overview of your selected PDF folder and retrieval setup")

    selected_folder = get_selected_folder()
    pdf_files = get_pdf_files(selected_folder)
    summary = get_vector_store_summary()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Selected Folder", str(selected_folder) if selected_folder else "Not selected")
    col2.metric("Number of PDFs", len(pdf_files))
    col3.metric("Indexed Chunks", summary["chunk_count"])
    col4.metric("Embedding Model", Config.EMBEDDING_MODEL)
    col5.metric("LLM Model", Config.LLM_MODEL)

    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        with st.container():
            st.subheader("System Snapshot")
            st.write(f"- Vector Database: {summary['vector_db']}")
            st.write(f"- Embedding Dimension: {summary['embedding_dimension']}")
            st.write(f"- Top-K Retrieval: {summary['top_k']}")
    with col_b:
        with st.container():
            st.subheader("Quick Actions")
            st.info("Select a PDF folder, build the index, and then ask questions from the AI chat page.")


def render_select_pdf_folder() -> None:
    """Render the folder selection page for the PDF directory workflow."""
    st.header("📂 Select PDF Folder")
    st.caption("Choose a directory that contains one or more PDF files")

    selected_folder = st.text_input(
        "Folder path",
        value=st.session_state.get("selected_folder", ""),
        placeholder=r"C:\Users\Padalingam\Documents\PDFs",
    )
    st.session_state["selected_folder"] = selected_folder

    if st.button("Browse Folder", width="stretch"):
        try:
            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            chosen_folder = filedialog.askdirectory()
            root.destroy()
            if chosen_folder:
                st.session_state["selected_folder"] = chosen_folder
                st.success("Folder selected successfully.")
        except Exception as exc:
            st.warning(f"Folder browser is not available in this environment: {exc}")

    st.divider()

    folder_path = get_selected_folder()
    if folder_path is None:
        st.info("Enter a folder path or browse for one to continue.")
        return

    if not folder_path.exists():
        st.error("The selected folder does not exist.")
        return

    if not folder_path.is_dir():
        st.error("The selected path is not a directory.")
        return

    pdf_files = get_pdf_files(folder_path)
    if not pdf_files:
        st.warning("No PDF files were found in the selected folder.")
        return

    st.success("Valid PDF folder detected.")
    st.write(f"**Folder path:** {folder_path}")
    st.write(f"**Number of PDF files:** {len(pdf_files)}")

    with st.expander("PDF Files"):
        for pdf_file in pdf_files:
            st.write(f"- {pdf_file.name}")


def render_build_knowledge_base() -> None:
    """Render the ingestion page for building the vector database."""
    st.header("🧠 Build Knowledge Base")
    st.caption("Index the selected PDF folder directly into the FAISS knowledge base")

    selected_folder = get_selected_folder()
    if selected_folder is None:
        st.info("Select a folder first before building the knowledge base.")
        return

    if not selected_folder.exists() or not selected_folder.is_dir():
        st.warning("Please select a valid folder path.")
        return

    pdf_files = get_pdf_files(selected_folder)
    if not pdf_files:
        st.warning("No PDF files were found in the selected folder.")
        return

    if st.button("Build Knowledge Base", type="primary", width="stretch"):
        with st.spinner("Building the knowledge base. This may take a moment..."):
            try:
                ingest_documents(selected_folder)
            except Exception as exc:
                st.error(f"Indexing failed: {exc}")
            else:
                st.success("Knowledge base built successfully.")


def render_ai_chat() -> None:
    """Render the chat experience backed by the existing RAG chain."""
    st.header("💬 AI Chat")
    st.caption("Ask a question about your selected PDF documents")

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("sources"):
                with st.expander("Retrieved Sources"):
                    for index, source in enumerate(message["sources"], start=1):
                        st.write(f"{index}. {source['title']}")
                        st.caption(f"Page: {source['page']}")
                        st.write(source["content"])

    prompt = st.chat_input("Ask something about your documents")
    if prompt:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Searching the knowledge base..."):
            try:
                result = ask(prompt)
                answer = result.get("answer", "")
                documents = result.get("documents", [])
            except Exception as exc:
                answer = f"I couldn't generate a response right now. Error: {exc}"
                documents = []

        sources = []
        for document in documents:
            metadata = document.metadata or {}
            sources.append(
                {
                    "title": Path(metadata.get("source", "Unknown")).name,
                    "page": metadata.get("page") or metadata.get("page_number") or "N/A",
                    "content": (document.page_content or "")[:300],
                }
            )

        assistant_message = {"role": "assistant", "content": answer, "sources": sources}
        st.session_state.chat_history.append(assistant_message)
        with st.chat_message("assistant"):
            st.markdown(answer)
            if sources:
                with st.expander("Retrieved Sources"):
                    for index, source in enumerate(sources, start=1):
                        st.write(f"{index}. {source['title']}")
                        st.caption(f"Page: {source['page']}")
                        st.write(source["content"])


def render_document_library() -> None:
    """Render the PDF inventory for the selected folder."""
    st.header("📄 Document Library")
    st.caption("All PDFs discovered in the selected folder")

    selected_folder = get_selected_folder()
    pdf_files = get_pdf_files(selected_folder)
    if not pdf_files:
        st.info("No PDFs are available yet for the selected folder.")
        return

    rows = []
    for pdf_file in pdf_files:
        stat = pdf_file.stat()
        rows.append(
            {
                "Filename": pdf_file.name,
                "Size (KB)": round(stat.st_size / 1024, 1),
                "Last Modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
            }
        )

    st.dataframe(rows, width="stretch")


def render_vector_database() -> None:
    """Render the vector database information page."""
    st.header("📦 Vector Database")
    st.caption("Current FAISS index and retrieval configuration")

    summary = get_vector_store_summary()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Embedding Model", summary["embedding_model"])
    col2.metric("Embedding Dimension", summary["embedding_dimension"])
    col3.metric("Vector Database", summary["vector_db"])
    col4.metric("Top-K Retrieval", summary["top_k"])

    st.divider()
    st.subheader("Index Summary")
    st.write(f"- Number of Documents: {summary['document_count']}")
    st.write(f"- Number of Chunks: {summary['chunk_count']}")
    st.write(f"- Storage Path: {INDEX_DIR}")


def render_settings() -> None:
    """Render the configuration settings page."""
    st.header("⚙ Settings")
    st.caption("Current application configuration values")

    settings = {
        "Base Directory": Config.BASE_DIR,
        "Data Directory": Config.DATA_DIR,
        "FAISS Index Directory": Config.FAISS_INDEX_DIR,
        "LLM Model": Config.LLM_MODEL,
        "Embedding Model": Config.EMBEDDING_MODEL,
        "Chunk Size": Config.CHUNK_SIZE,
        "Chunk Overlap": Config.CHUNK_OVERLAP,
        "Top-K": Config.TOP_K,
    }

    st.json(settings)


def main() -> None:
    """Main application entry point."""
    st.set_page_config(page_title="RAG Studio", page_icon="🧠", layout="wide")
    ensure_directories()
    init_session_state()

    st.markdown(
        """
        <style>
        .stApp { background: linear-gradient(135deg, #0f172a 0%, #111827 100%); }
        .block-container { padding-top: 2rem; padding-bottom: 2rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.image(
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=120&q=80",
        width="stretch",
    )
    st.sidebar.title("RAG Studio")
    st.sidebar.caption("Local document intelligence")

    pages = {
        "🏠 Dashboard": render_dashboard,
        "📂 Select PDF Folder": render_select_pdf_folder,
        "🧠 Build Knowledge Base": render_build_knowledge_base,
        "💬 AI Chat": render_ai_chat,
        "📄 Document Library": render_document_library,
        "📦 Vector Database": render_vector_database,
        "⚙ Settings": render_settings,
    }

    selected_page = st.sidebar.radio("Navigate", list(pages.keys()))
    pages[selected_page]()


if __name__ == "__main__":
    main()
