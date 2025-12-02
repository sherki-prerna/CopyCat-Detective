import React from "react";
import "./PairwiseResults.css";

export default function PairwiseResults({ matrix, filenames }) {
  // Convert matrix -> list of pairs
  const pairs = [];

  for (let i = 0; i < filenames.length; i++) {
    for (let j = i + 1; j < filenames.length; j++) {
      pairs.push({
        file1: filenames[i],
        file2: filenames[j],
        score: matrix[i][j],
      });
    }
  }

  // Sort by similarity highest → lowest
  pairs.sort((a, b) => b.score - a.score);

  // Helper to avoid NaN
  function safeScore(value) {
    const num = Number(value);
    return isNaN(num) ? 0 : num;
  }

  // Function for text explanation
  function explanation(score) {
    const p = Math.round(score * 100);

    if (p === 100)
      return "These files are identical. High plagiarism detected.";
    if (p >= 70)
      return "High similarity. These files likely contain copied content.";
    if (p >= 40)
      return "Moderate similarity. Review recommended.";
    if (p >= 20) return "Some overlap found, but mostly safe.";
    return "Low similarity. No plagiarism detected.";
  }

  return (
    <div className="pairs-container">
      <h2>Similarity Results</h2>
      {pairs.map((pair, index) => {
        const cleanedScore = safeScore(pair.score);
        const percentage = Math.round(cleanedScore * 100);

        return (
          <div className="pair-card" key={index}>
            <h3>
              {pair.file1} <span style={{ color: "#999" }}>vs</span>{" "}
              {pair.file2}
            </h3>
            <div className="pair-score">{percentage}% Similarity</div>
            <p className="pair-explanation">
              {explanation(cleanedScore)}
            </p>
          </div>
        );
      })}
    </div>
  );
}
