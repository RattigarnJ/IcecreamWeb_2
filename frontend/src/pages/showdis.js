import '../App.css';
import React from "react";
import { useState, useEffect, useMemo } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import logo from "../components/back.png";
import logosearch from "../components/search.png"

const ShowST = () => {

    const navigate = useNavigate();
    const [images, setImages] = useState([]);

    useEffect(() => {
        fetchPredictions();
    }, []);

    const fetchPredictions = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:5000/predict_all");
            setImages(response.data);
        } catch (error) {
            console.error("Error fetching predictions:", error);
        }
    };

    return (
        <div className="prediction-report">
            <div className="prediction-grid">
                {images.map((img, index) => (
                    <div key={index} className="prediction-card">
                        <img src={img.path} alt={img.filename} className="image-placeholder"/>
                        <div className="button-container">
                            <div
                                className="circle-button"
                            >
                                <img src={logosearch} alt="logo" style={{ width: '15px', cursor: 'pointer' }} />
                            </div>
                        </div>
                        <div className="prediction-info" >
                            <p>
                                <strong>name :</strong> {img.filename || '-'}
                            </p>
                            <p>
                                <strong>prediction result :</strong> {img.prediction === 1 ? 'Not Cabinet' : img.prediction === 2 ? 'Standing Cabinet' : 'Lying down Cabinet' || '-'}
                            </p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ShowST;