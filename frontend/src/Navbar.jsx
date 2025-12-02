import logo from "./assets/ChatGPT Image Nov 28, 2025, 10_15_29 PM-min.png";
import "./style.css";
export default function Navbar() {
  return (
    <div className="navbar">
      <img src={logo} alt="CopyCat Detective Logo" className="nav-logo" />
      <span className="nav-title">CopyCat Detective</span>
    </div>
  );
}
