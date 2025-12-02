from flask import Flask, request, jsonify
from flask_cors import CORS
from similarity import compute_similarity

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "CopyCat Detective Backend Active!"
    }

@app.post("/upload")
def upload():
    files = request.files.getlist("files")
    result = compute_similarity(files)
    return jsonify(result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
