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
            <p className='Text-Welcome'>WELCOME</p>
            <div className='Box-PS' onClick={handleShow}>
            <div className='Circle' onClick={handleShow}>
                <img src={logoshow} alt="logo" style={{ width: '50px', marginTop: '25px', marginLeft: '25px', cursor: 'pointer'}} onClick={handleShow}/>   
            </div>
            <p className='Text-PS'>SHOW IMAGES</p>
            </div>
        </div>
    );
};

export default Home;