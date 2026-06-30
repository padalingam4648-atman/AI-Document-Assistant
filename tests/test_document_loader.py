from src.document_loader import load_documents


def test_load_documents_empty(tmp_path):
    # create empty dir
    result = load_documents(str(tmp_path))
    assert isinstance(result, list)
    assert result == []


def test_load_documents_with_txt(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("hello world")
    results = load_documents(str(tmp_path))
    assert len(results) == 1
    assert "hello world" in results[0]
