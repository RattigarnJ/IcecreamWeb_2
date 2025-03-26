import React from "react";
import { Image } from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();

  const handleHome = () => {
    navigate("/home");
  };

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <p style={{ fontWeight: 'bold', fontSize: '16px', cursor:'pointer' }} onClick={handleHome}>ICE CREAM CABINET</p>
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
            <Link to="/">LOGOUT</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
