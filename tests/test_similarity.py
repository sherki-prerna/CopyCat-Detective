import io
import numpy as np
from backend import similarity


# Test 1: Less than 2 files should return error
def test_less_than_two_files():
    fake_file = io.BytesIO(b"Hello world")
    result = similarity.compute_similarity([fake_file])

    assert "error" in result
    assert "at least" in result["error"].lower()
    assert ("2" in result["error"]) or ("two" in result["error"].lower())


# Test 2: Similarity matrix shape/values should be valid
def test_similarity_matrix(monkeypatch):
    fake_file1 = io.BytesIO(b"text one")
    fake_file2 = io.BytesIO(b"text two")

    class FakeModel:
        def encode(self, texts, convert_to_numpy=True, show_progress_bar=False):
            return np.array([[1.0, 0.0], [0.0, 1.0]])

    monkeypatch.setattr(similarity, "get_model", lambda: FakeModel())

    result = similarity.compute_similarity([fake_file1, fake_file2])

    assert "matrix" in result
    assert len(result["matrix"]) == 2
    assert len(result["matrix"][0]) == 2
    assert result["matrix"][0][0] == 1.0
    assert 0 <= result["matrix"][0][1] <= 1
