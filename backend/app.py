from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
try:
    from backend.similarity import compute_similarity
except ImportError:
    from similarity import compute_similarity

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

# ---------------- API ----------------

@app.route("/api/health")
def health_check():
    return jsonify({"status": "ok"})

@app.route("/api/similarity", methods=["POST"])
def similarity_api():
    uploaded_files = request.files.getlist("files")

    if len(uploaded_files) < 2:
        return jsonify({"error": "Please upload at least two files"}), 400

    try:
        result = compute_similarity(uploaded_files)
    except Exception as exc:
        return jsonify({"error": f"Similarity computation failed: {exc}"}), 500

    if "error" in result:
        return jsonify(result), 500

    return jsonify(result)


# ---------------- FRONTEND ----------------

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    file_path = os.path.join("static", path)
    if path != "" and os.path.exists(file_path):
        return send_from_directory("static", path)
    return send_from_directory("static", "index.html")

# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
