import '../App.css';
import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import logoload from "../components/download.png";
import logoshow from "../components/dashboard.png";

const Home = () => {

    const navigate = useNavigate();

    const handlePull = () => {
        navigate("/Pull");
    };

    const handleShow = () => {
        navigate("/Show");
    };

    return (
        <div className="Containner-home">
            <p className='Text-Welcome'>Menber</p>
        </div>
    );
};

export default Home;