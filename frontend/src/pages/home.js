import '../App.css';
import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

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
                <p className='Text-H'>ICE CREAM CABINET</p>
            <div className='Div-butcon'>
                    <button
                        className='Button-styleCon'
                        onClick={handlePull}
                    >
                    Pull images
                    </button>
                    <button
                        className='Button-styleCon'
                        onClick={handleShow}
                    >
                    Show images
                    </button>
            </div>
        </div>
    );
};

export default Home;