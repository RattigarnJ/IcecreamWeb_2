import '../App.css';
import React from "react";
import { useState, useEffect, useMemo } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import logo from "../components/back.png";


const ShowST = () => {

    const navigate = useNavigate();
    const [images, setImages] = useState([]);

    const handleShowImg = (e) => {
      const fetchImages = async () => {
        try {
          const response = await axios.post("http://127.0.0.1:5000/predict",);
          setImages(response.data.images);
        } catch (error) {
          console.error("Error fetching images:", error);
        }
        };
    }

    return (
        <div className="Containner-showdis">
            <p className='Text-H'>Prediction</p>
            <button
                className='Button-stylePredict'
                onClick = {handleShowImg}
            >
            Predict!
            </button>
            <div className='Div-back'>
            <Link to="/show" className="logo">
                <img src={logo} alt="" className="Back-ele" />
            </Link>
            <p className='Back-text'>back</p>
            </div>
        </div>
    );
};

export default ShowST;