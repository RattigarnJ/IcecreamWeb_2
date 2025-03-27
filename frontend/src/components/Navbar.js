import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

const Navbar = ({ setIsAuthenticated }) => {
  const navigate = useNavigate();
  const role = localStorage.getItem("role");

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("role"); // ✅ ลบ role ออกจาก localStorage
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
          {role == "Dev" && ( // ✅ ซ่อน "PULL" สำหรับ User
            <li>
              <Link to="/menber">MENBER</Link>
            </li>
          )}
          {role !== "User" && ( // ✅ ซ่อน "PULL" สำหรับ User
            <li>
              <Link to="/pull">PULL</Link>
            </li>
          )}
          <li>
            <Link to="/show">SHOW</Link>
          </li>
          {role == "Dev" && ( // ✅ ซ่อน "PULL" สำหรับ User
          <li>
            <Link to="/register">Sign In</Link>
          </li>
          )}
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
