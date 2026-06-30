from src.ingest import ingest_documents


def test_ingest_runs_on_empty_dir(tmp_path):
    db_path = str(tmp_path / "vec.db")
    # should run without raising
    ingest_documents(str(tmp_path), db_path)
