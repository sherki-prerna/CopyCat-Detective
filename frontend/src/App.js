import React, { useState } from "react";
import Navbar from "./Navbar";
import UploadBox from "./UploadBox";
import PairwiseResults from "./PairwiseResults";
import "./style.css";
import { useEffect } from "react";
import Swal from "sweetalert2";
import detectiveCat from "./assets/ChatGPT Image Nov 28, 2025, 10_15_29 PM-min.png";

export default function App() {
  useEffect(() => {
  Swal.fire({
    title: "Welcome to CopyCat Detective!",
    text: "Catching Copycats Since Day One 🕵️‍♂️📄",
    imageUrl: detectiveCat,
    imageWidth: 150,
    confirmButtonText: "Start",
    confirmButtonColor: "#1b63ff",
    showClass: {
      popup: "animate__animated animate__zoomIn animate__faster"
    },
    hideClass: {
      popup: "animate__animated animate__zoomOut animate__faster"
    }
  });
}, []);

  const [matrix, setMatrix] = useState(null);
  const [filenames, setFilenames] = useState([]);

  const handleMatrix = (m, f) => {
    setMatrix(m);
    setFilenames(f);
  };

  return (
    <>
      <Navbar />

      {/* Section 2 */}
      <UploadBox onMatrix={handleMatrix} />

      {/* Section 3 */}
      <PairwiseResults matrix={matrix} filenames={filenames} />
    </>
  );
}
