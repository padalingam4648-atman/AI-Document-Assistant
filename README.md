# 🤖 AI Document Assistant (Local RAG)

A Local Retrieval-Augmented Generation (RAG) application built with **Python**, **LangChain**, **Ollama**, **Llama 3.2**, **FAISS**, and **Streamlit**.

The application allows users to select a local folder containing PDF documents, build a vector database, and ask natural language questions about the document contents using a fully offline Large Language Model.

---

# ✨ Features

- 📂 Select any local folder containing PDF files
- 📄 Automatic PDF document loading
- ✂️ Intelligent document chunking
- 🧠 Local embeddings using Nomic Embed Text
- 📦 FAISS vector database
- 🔍 Semantic search
- 🤖 Offline AI responses using Llama 3.2
- 💬 Modern Streamlit interface
- 📚 Document Library
- 📊 Vector Database Information
- 🔒 100% Offline (No OpenAI API)

---

# 🏗 Project Architecture

```
                  PDF Folder
                      │
                      ▼
              Document Loader
                      │
                      ▼
             Text Splitter
                      │
                      ▼
           Nomic Embed Text
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
             Llama 3.2 (Ollama)
                      │
                      ▼
               AI Generated Answer
```

---

# 📂 Project Structure

```
AI-Document-Assistant/

│
├── data/
│
├── faiss_index/
│
├── logs/
│
├── src/
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
│
├── app.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

### Programming Language

- Python

### Framework

- LangChain

### Frontend

- Streamlit

### Local LLM

- Ollama
- Llama 3.2

### Embedding Model

- Nomic Embed Text (768 Dimensions)

### Vector Database

- FAISS

### Document Processing

- PyPDFLoader
- RecursiveCharacterTextSplitter

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/padalingam4648-atman/AI-Document-Assistant.git

cd AI-Document-Assistant
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

---

## Download Models

```bash
ollama pull llama3.2
```

```bash
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

Expected output:

```
llama3.2

nomic-embed-text
```

---

# ▶ Running the Application

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The application will open automatically in your browser.

Default URL:

```
http://localhost:8501
```

---

# 📂 Using the Application

### Step 1

Open the **Select PDF Folder** page.

---

### Step 2

Choose a local folder containing PDF files.

Example:

```
C:\Users\Padalingam\Documents\PDFs
```

The application displays:

- Selected Folder
- Total PDFs
- PDF Names

---

### Step 3

Open the **Build Knowledge Base** page.

Click:

```
Build Knowledge Base
```

The application automatically:

- Loads all PDFs
- Splits documents into chunks
- Generates embeddings
- Creates the FAISS vector database
- Saves the vector index

---

### Step 4

Open the **AI Chat** page.

Ask questions like:

```
Explain the Mobi-Locator project.
```

```
What technologies are used in my AI project?
```

```
Summarize my resume.
```

The AI retrieves the most relevant document chunks and generates a context-aware response.

---

# 📄 Streamlit Pages

### 🏠 Dashboard

Displays:

- Total PDFs
- Document Chunks
- Embedding Model
- LLM Model
- Vector Database

---

### 📂 Select PDF Folder

- Browse local directory
- Validate PDF files
- Display PDF information

---

### 🧠 Build Knowledge Base

- Build FAISS index
- Generate embeddings
- Save vector database

---

### 💬 AI Chat

- Ask questions
- AI-generated responses
- Retrieved source documents
- Chat history

---

### 📄 Document Library

Displays:

- PDF Names
- File Size
- Last Modified Date

---

### 📦 Vector Database

Displays:

- Embedding Model
- Embedding Dimension
- Number of Chunks
- Vector Database
- Top-K Retrieval

---

### ⚙ Settings

Displays current configuration:

- Chunk Size
- Chunk Overlap
- Embedding Model
- LLM Model
- FAISS Directory

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

Generated Answer
```

---

# 📊 Development Phases

| Phase | Module | Status |
|--------|--------|--------|
| 1 | Project Setup | ✅ |
| 2 | Document Loader | ✅ |
| 3 | Text Splitter | ✅ |
| 4 | Embedding Model | ✅ |
| 5 | FAISS Vector Store | ✅ |
| 6 | Ingestion Pipeline | ✅ |
| 7 | Retriever | ✅ |
| 8 | Prompt Engineering | ✅ |
| 9 | LLM Integration | ✅ |
| 10 | RAG Chain | ✅ |
| 11 | Streamlit Interface | ✅ |
| 12 | RAG Optimization | 🚧 Planned |

---

# 🚀 Future Improvements

- Support DOCX, TXT, and Markdown
- Hybrid Search (BM25 + FAISS)
- Metadata Filtering
- MMR Retrieval
- Reranking
- Chunk Viewer
- Embedding Visualization
- Multi-User Authentication
- Conversation Memory
- Dark/Light Theme Toggle
- Export AI Responses

---

# 👨‍💻 Author

**Padalingam S**

Computer Science Engineer | Cyber Security | AI Engineering

### GitHub

https://github.com/padalingam4648-atman

### Portfolio

https://padalingam-portfolio.netlify.app

---

# ⭐ If you found this project useful, consider giving it a Star on GitHub!