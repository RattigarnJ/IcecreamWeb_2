import '../App.css';
import React from "react";
import { useState, button } from "react";
import { useNavigate } from "react-router-dom";

const Pull = () => {

    const navigate = useNavigate();

    const handleLogin = () => {
        navigate("/Login");
    };

    const handlePullST = () => {
        navigate("/pullst");
    };

    const handlePullLD = () => {
        navigate("/pullld");
    };

    return (
        <div className="Containner-pull">
            <p className='Text-H'>Choose the contract you want to pull</p>
            <div className='Div-butcon'>
            <button
                className='Button-styleCon'
                onClick={handlePullST}
            >
            Standing Contract
            </button>
            <button
                className='Button-styleCon'
                onClick={handlePullLD}
            >
            Lying down Contract
            </button>
            </div>
        </div>
    );
};

export default Pull;
