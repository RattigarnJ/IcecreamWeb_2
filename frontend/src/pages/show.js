import '../App.css';
import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Show = () => {

    const navigate = useNavigate();

    const handleShowST = () => {
        navigate("/showst");
    };

    const handleShowLD = () => {
        navigate("/showld");
    };

    return (
        <div className="Containner-show">
            <p className='Text-H'>Choose the contract you want to show</p>
            <div className='Div-butcon'>
            <button
                className='Button-styleCon'
                onClick={handleShowST}
            >
            Standing Contract
            </button>
            <button
                className='Button-styleCon'
                onClick={handleShowLD}
            >
            Lying down Contract
            </button>
            </div>
        </div>
    );
};

export default Show;