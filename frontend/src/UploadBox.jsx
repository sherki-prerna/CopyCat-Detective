import React, { useState } from "react";
import Swal from "sweetalert2";
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
      Swal.fire("Oops!", "Please upload at least two files.", "error");
      return;
    }

    const form = new FormData();
    files.forEach((file) => form.append("files", file));

    try {
      const res = await fetch("http://localhost:5000/api/similarity", {
        method: "POST",
        body: form,
      });

      const data = await res.json();

      if (data.error) {
        Swal.fire("Error", data.error, "error");
        return;
      }

      onMatrix(
        data.matrix,
        files.map((f) => f.name)
      );

      Swal.fire("Success!", "Similarity calculated!", "success");
    } catch (error) {
      console.error(error);
      Swal.fire("Error", "Could not reach the server!", "error");
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Assignment Files</h2>

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
