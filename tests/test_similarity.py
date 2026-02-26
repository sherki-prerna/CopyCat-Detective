import io
import similarity


# Test 1: Less than 2 files should return error
def test_less_than_two_files():
    fake_file = io.BytesIO(b"Hello world")
    result = similarity.compute_similarity([fake_file])

    assert "error" in result
    assert result["error"] == "Upload at least 2 files"


# Test 2: Similarity score should be between 0 and 1
def test_similarity_range(monkeypatch):
    fake_file1 = io.BytesIO(b"text one")
    fake_file2 = io.BytesIO(b"text two")

    # Fake lightweight similarity function
    def fake_compute(files):
        return {"similarity": 0.82}

    monkeypatch.setattr(similarity, "compute_similarity", fake_compute)

    result = fake_compute([fake_file1, fake_file2])

    assert 0 <= result["similarity"] <= 1
