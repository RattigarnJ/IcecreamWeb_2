import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

const Navbar = ({ setIsAuthenticated }) => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    setIsAuthenticated(false); // ✅ อัปเดต state
    navigate("/", { replace: true });
  };

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <p style={{ fontWeight: 'bold', fontSize: '16px', cursor: 'pointer' }} onClick={() => navigate("/home")}>
          ICE CREAM CABINET
        </p>
      </div>
      <div className="navbar-right">
        <ul className="nav-links">
          <li>
            <Link to="/pull">PULL</Link>
          </li>
          <li>
            <Link to="/show">SHOW</Link>
          </li>
          <li>
            <button onClick={handleLogout} style={{ background: "none", border: "none", cursor: "pointer", color: "red" }}>
              LOGOUT
            </button>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
