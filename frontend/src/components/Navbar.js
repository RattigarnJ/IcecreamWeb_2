import React from "react";
import { Image } from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";
import logo from "./ice-cream.png";

const Navbar = () => {
  return (
    <nav className="navbar">
        <div className="navbar-left">
        <Link to="/" className="logo">
        <img src={logo} alt="" className="logo-img" />
        </Link>
        </div>
        <div className="navbar-right">
        <ul className="nav-links">
            <li>
            <Link to="/pull">Pull</Link>
            </li>
            <li>
            <Link to="/show">Show</Link>
            </li>
            <li>
            <Link to="/login">Login</Link>
            </li>
        </ul>
        </div>
    </nav>
  );
};

export default Navbar;
