import '../App.css';
import React from "react";
import { useState, useEffect, useMemo } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import logo from "../components/back.png";

const Show = () => {

    const navigate = useNavigate();

    const [selectedDateStart, setSelectedDateStart] = useState("");
    const [selectedDateStop, setSelectedDateStop] = useState("");
    const [periodday, setPeriodday] = useState(0);
    const [message, setMessage] = useState("");
    const [mode, setMode] = useState("");

    const splitDate = (dateString1, dateString2) => {
        const [year1, month1, day1] = dateString1.split("-");
        const [year2, month2, day2] = dateString2.split("-")
        return { year1, month1, day1, day2 };
    };

    function getColumnAndRow(selectedDate) {
        if (!selectedDate) {
            console.error("Error: selectedDate is undefined or null");
            return { day: null, column: null, row: null };
        }

        const dateObj = new Date(selectedDate);
        if (isNaN(dateObj.getTime())) {
            console.error(`Error: Invalid Date format - selectedDate: ${selectedDate}`);
            return { day: null, column: null, row: null };
        }

        let weekday = (dateObj.getDay()) % 7 + 1;
        let column = weekday;
        let day = dateObj.getDate();

        const firstDayOfMonth = new Date(dateObj.getFullYear(), dateObj.getMonth(), 1);
        let firstDayColumn = ((firstDayOfMonth.getDay() + 6) % 7) + 1;
        let dayPosition = day + (firstDayColumn - 1);
        let row = Math.ceil(dayPosition / 7);

        return { day, column, row };
    }

    const { year1, month1 } = splitDate(selectedDateStart, selectedDateStop);

    useEffect(() => {
        if (selectedDateStart && selectedDateStop) {
            const { day1, day2 } = splitDate(selectedDateStart, selectedDateStop);
            setPeriodday(day2 - day1);
            setMode("st");
        }
    }, [selectedDateStart, selectedDateStop]);

    const { day, column, row } = useMemo(() => getColumnAndRow(selectedDateStart), [selectedDateStart]);

    const runRPA = async () => {
        try {
            const response = await axios.post("http://localhost:5000/run_rpa", {
                row: row,
                column: column,
                month1: month1,
                year1: year1,
                periodday: periodday,
                moderun: mode,
            });

            setMessage(response.data.message);

            navigate("/pullsuccess");

        } catch (error) {
            console.error("Error:", error);
            setMessage("Failed to start RPA");
        }
    };

    return (
        <div className="Containner-pull">
            <p className='Text-PS-H-ST' style={{ alignSelf: 'center' }}>STANDING CONTRACT</p>
            <p className='Text-PS-H-ST' style={{ marginTop: '-35px', alignSelf: 'center' }}>PULL IMAGES</p>
            <p style={{ marginLeft: '-480px'}}>Day - Start</p>
            <input
                type="date"
                value={selectedDateStart}
                onChange={(e) => setSelectedDateStart(e.target.value)}
                min="2024-01-01"
                max="2025-12-31"
                className='Date-picker'
                required
            />
            <p style={{ marginLeft: '-480px' }}>Day - Stop</p>
            <input
                type="date"
                value={selectedDateStop}
                onChange={(e) => setSelectedDateStop(e.target.value)}
                min="2024-01-01"
                max="2025-12-31"
                className='Date-picker'
                required
            />
            <button
                className='Button-Pull'
                onClick={runRPA}
            >
                PULL
            </button>
            <div className='Div-back' style={{ position: 'fixed' }}>
                <Link to="/pull" className="logo">
                    <img src={logo} alt="" className="Back-ele" style={{}} />
                    <p className='Back-text' style={{ position: 'fixed' }}>BACK</p>
                </Link>
            </div>
        </div>
    );
};

export default Show;