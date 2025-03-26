import '../App.css';
import React from "react";
import { useState, useEffect, useMemo } from "react";
import { useNavigate, Link, Navigate } from "react-router-dom";
import axios from "axios";
import logo from "../components/back.png";

const PullSuccess = () => {

    const navigate = useNavigate();

    const handleShow = () => {
        navigate("/show");
    };

    return (
        <div className='Containner-pullsuccess'>
            <p style={{fontSize: '40px', fontWeight: 'bold'}}>PULL IMAGES SUCCESS</p>
            <p style={{marginTop: '-30px', cursor:'pointer'}} onClick={handleShow}>Let's show images</p>
        </div>
    );
};

export default PullSuccess;