import '../App.css';
import React from "react";
import { useState, button, } from "react";

const Login = () => {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const loginclick = () => {
        alert(`Logging in as: ${username} and ${password}`);
    }

    return (
        <div className="Containner-login">
            <p className="Text-H">WELCOME</p>
            <p className="Text-D">please login</p>
            <p className="Text-UP">username</p>
            <div className="Input-div">
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="username"
                className= "Input-Box"/>
            </div>
            <p className="Text-UP">password</p>
            <div className="Input-div">
            <input
                type="text"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="password"
                className= "Input-Box"/>
            </div>
            <button
                className='Button-styleLogin'
                onClick={loginclick}
            >
            Login
            </button>
        </div>
    );
};

export default Login;