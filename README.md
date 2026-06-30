# 🤖 AI Document Assistant (Local RAG)

A Local Retrieval-Augmented Generation (RAG) system built with **Python**, **LangChain**, **FAISS**, **Ollama**, and **Llama 3.2**.

The application allows users to chat with their own PDF documents completely offline by retrieving relevant document sections and generating context-aware answers using a local Large Language Model.

---

# 📌 Features

- 📄 Load multiple PDF documents
- ✂️ Automatic document chunking
- 🧠 Local embeddings using Ollama (`nomic-embed-text`)
- 🔍 FAISS vector database for semantic search
- 🤖 Local LLM using Llama 3.2
- 💬 Interactive question-answering
- 🔒 Fully offline (No OpenAI API required)
- 📚 Modular and scalable architecture

---

# 🏗️ Project Architecture

```
                PDF Documents
                      │
                      ▼
              Document Loader
                      │
                      ▼
              Text Splitter
                      │
                      ▼
            Ollama Embeddings
                      │
                      ▼
              FAISS Vector Store
                      │
                      ▼
                 Retriever
                      │
                      ▼
               Prompt Builder
                      │
                      ▼
                Llama 3.2 (LLM)
                      │
                      ▼
              AI Generated Answer
```

---

# 📂 Project Structure

```
Local-RAG/
│
├── data/
│   ├── docs/
│   ├── pdfs/
│   └── txt/
│
├── db/
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── logs/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── utils.py
│   ├── logger.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── ingest.py
│   ├── retriever.py
│   ├── prompt.py
│   ├── llm.py
│   └── rag_chain.py
│
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_document_loader.py
│   ├── test_embedding.py
│   ├── test_ingest.py
│   ├── test_llm.py
│   ├── test_loader.py
│   ├── test_prompt.py
│   ├── test_rag_chain.py
│   ├── test_retriever.py
│   ├── test_text_splitter.py
│   ├── test_utils.py
│   └── test_vector_store.py
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Technologies Used

### Programming Language

- Python 3.12

### Frameworks

- LangChain

### Local LLM

- Ollama
- Llama 3.2

### Embedding Model

- nomic-embed-text

### Vector Database

- FAISS

### Document Processing

- PyPDFLoader
- RecursiveCharacterTextSplitter

---

# 🚀 Installation

## 1 Clone Repository

```bash
git clone https://github.com/yourusername/AI-Document-Assistant.git

cd AI-Document-Assistant
```

---

## 2 Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

---

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Install Ollama

Download:

https://ollama.com

---

## 5 Pull Models

```bash
ollama pull llama3.2
```

```bash
ollama pull nomic-embed-text
```

Verify

```bash
ollama list
```

Expected

```
llama3.2
nomic-embed-text
```

---

# 📄 Build Knowledge Base

Run

```bash
python app.py
```

Choose

```
1. Build Knowledge Base
```

Select the folder containing PDF files.

The system will

- Load PDFs
- Split into chunks
- Generate embeddings
- Create FAISS index
- Save vector database

---

# 💬 Chat With Documents

Run

```bash
python app.py
```

Choose

```
2. Chat with Documents
```

Example

```
Explain the Mobi-Locator Project
```

Output

```
Project Overview

Mobi-Locator is an Android-based mobile security application
that enables remote device control using SMS commands.

Features

• GPS Tracking
• SMS Commands
• Background Services

Tech Stack

• Kotlin
• Android SDK
• BroadcastReceiver

Source

Resume.pdf
Page 1
```

---

# 🧠 RAG Workflow

```
Question

↓

Retriever

↓

Relevant Chunks

↓

Prompt Builder

↓

Llama 3.2

↓

Answer
```

---

# 📊 Development Phases

| Phase | Module | Status |
|--------|--------|--------|
| 1 | Config | ✅ |
| 2 | Document Loader | ✅ |
| 3 | Text Splitter | ✅ |
| 4 | Embedding | ✅ |
| 5 | FAISS Vector Store | ✅ |
| 6 | Ingest Pipeline | ✅ |
| 7 | Retriever | ✅ |
| 8 | Prompt Builder | ✅ |
| 9 | LLM | ✅ |
| 10 | RAG Chain | ✅ |
| 11 | Application | ✅ |
| 12 | RAG Optimization | 🚧 Planned |

---

# 📈 Future Improvements

- Streamlit Web UI
- Conversation Memory
- Chat History
- Hybrid Search (BM25 + FAISS)
- MMR Retrieval
- Reranking
- Multi-format Document Support (PDF, DOCX, TXT)
- Metadata Filtering
- Source Highlighting
- REST API using FastAPI

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Padalingam S**

Computer Science Engineer | Cyber Security | AI Engineering

GitHub:
https://github.com/padalingam4648-atman

Portfolio:
https://padalingam-portfolio.netlify.app