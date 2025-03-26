import '../App.css';
import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import logoload from "C:\\Users\\Ratti\\myicecreamapp\\frontend\\src\\components\\download.png";
import logoshow from "C:\\Users\\Ratti\\myicecreamapp\\frontend\\src\\components\\dashboard.png";

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
            <div style={{display: 'flex', flexDirection: 'row'}}>
            <div className='Box-PS' style={{marginRight: '50px'}} onClick={handlePull}>
            <div className='Circle' onClick={handlePull}>
                <img src={logoload} alt="logo" style={{ width: '50px', marginTop: '25px', marginLeft: '25px', cursor: 'pointer'}} onClick={handlePull}/>   
            </div>
            <p className='Text-PS'>PULL IMAGES</p>
            </div>
            <div className='Box-PS' onClick={handleShow}>
            <div className='Circle' onClick={handleShow}>
                <img src={logoshow} alt="logo" style={{ width: '50px', marginTop: '25px', marginLeft: '25px', cursor: 'pointer'}} onClick={handleShow}/>   
            </div>
            <p className='Text-PS'>SHOW IMAGES</p>
            </div>
            </div>
        </div>
    );
};

export default Home;