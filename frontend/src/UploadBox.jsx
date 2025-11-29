import React, { useState } from "react";
import axios from "axios";
import "./style.css";

export default function UploadBox({ onMatrix }) {
  const [files, setFiles] = useState([]);
  const [dragActive, setDragActive] = useState(false);

  const handleFiles = (selected) => {
    setFiles((prev) => [...prev, ...selected]);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setDragActive(false);
    handleFiles(e.dataTransfer.files);
  };

  const handleUpload = async () => {
    if (files.length < 2) {
      alert("Please upload at least two files.");
      return;
    }

    const form = new FormData();
    files.forEach((file) => form.append("files", file));

    const res = await axios.post("http://localhost:5000/upload", form, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    onMatrix(
      res.data,
      files.map((f) => f.name)
    );
  };

  return (
    <div className="upload-container">
      <h2>Upload Assignment Files</h2>

      {/* Drag & Drop Box */}
      <div
        className={`dropzone ${dragActive ? "active" : ""}`}
        onDragOver={(e) => {
          e.preventDefault();
          setDragActive(true);
        }}
        onDragLeave={() => setDragActive(false)}
        onDrop={handleDrop}
      >
        <p>Drag & Drop files here</p>
        <span>or</span>

        <label className="browse-btn">
          Select Files
          <input
            type="file"
            multiple
            hidden
            onChange={(e) => handleFiles(e.target.files)}
          />
        </label>
      </div>

      {/* Show selected files */}
      {files.length > 0 && (
        <div className="file-list">
          <h4>Selected Files:</h4>
          <ul>
            {files.map((f, i) => (
              <li key={i}>{f.name}</li>
            ))}
          </ul>
        </div>
      )}

      <button className="analyze-btn" onClick={handleUpload}>
        Analyze Similarity
      </button>
    </div>
  );
}
