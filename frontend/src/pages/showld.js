import '../App.css';
import React from "react";
import { useState, useEffect, useMemo } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import logo from "../components/back.png";

const ShowLD = () => {

    const navigate = useNavigate();

    const [selectedDateStart, setSelectedDateStart] = useState("");
    const [selectedDateStop, setSelectedDateStop] = useState("");
    const [message, setMessage] = useState("");
    const [periodday, setPeriodday] = useState("");
    const [mode, setMode] = useState("");

    const splitDate = (dateString1, dateString2) => {
        const [year1, month1, day1] = dateString1.split("-");
        const [year2, month2, day2] = dateString2.split("-")
        return {day1, day2};
    };

    useEffect(() => {
            if (selectedDateStart && selectedDateStop) {
                const { day1, day2 } = splitDate(selectedDateStart, selectedDateStop);
                setPeriodday(day2 - day1); 
                setMode("ld");
            }
        }, [selectedDateStart, selectedDateStop]);

    const getShow = async () => {
        try {
          const response = await axios.post("http://localhost:5000/predict", {
            datestart: selectedDateStart,
            datestop: selectedDateStop,
            periodday: periodday,
            mode: mode,
          });

          navigate("/showdis");

          setMessage(response.data.message);
        } catch (error) {
            console.error("Error:", error);
            setMessage("Failed to show");
        }
    };

    return (
        <div className="Containner-show">
            <p>Lying down Contract - Show images</p>
            <p className='Text-date'>Day - Start</p>
            <input
                type="date"
                value={selectedDateStart}
                onChange={(e) => setSelectedDateStart(e.target.value)}
                min="2024-01-01" 
                max="2025-12-31" 
                className="Date-picker"
            />
            <p className='Text-date'>Day - Stop</p>
            <input
                type="date"
                value={selectedDateStop}
                onChange={(e) => setSelectedDateStop(e.target.value)}
                min="2024-01-01" 
                max="2025-12-31" 
                className="Date-picker"
            />
            <button
                className='Button-stylePull'
                onClick={getShow}
            >
            Show Images
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

export default ShowLD;