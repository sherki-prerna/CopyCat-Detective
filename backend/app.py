from flask import Flask,request,jsonify,send_from_directory
from flask_cors import CORS
import similarity
# from auth import auth



app = Flask(__name__, static_folder='build', static_url_path='/')
CORS(app)

# app.register_blueprint(auth)
@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, 'index.html')
@app.post("/upload")
def upload():
    files = request.files.getlist("files")
    result = similarity.compute_similarity(files)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)