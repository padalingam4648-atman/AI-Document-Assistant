from src.config import Config

print("=" * 50)
print("Local RAG Configuration")
print("=" * 50)

print(f"Base Directory     : {Config.BASE_DIR}")
print(f"Data Directory     : {Config.DATA_DIR}")
print(f"PDF Directory      : {Config.PDF_DIR}")
print(f"DOC Directory      : {Config.DOC_DIR}")
print(f"TXT Directory      : {Config.TXT_DIR}")
print(f"FAISS Directory    : {Config.FAISS_INDEX_DIR}")
print(f"LLM Model          : {Config.LLM_MODEL}")
print(f"Embedding Model    : {Config.EMBEDDING_MODEL}")
print(f"Chunk Size         : {Config.CHUNK_SIZE}")
print(f"Chunk Overlap      : {Config.CHUNK_OVERLAP}")
print(f"Top K              : {Config.TOP_K}")