import '../App.css';
import React from "react";
import { useState, button, } from "react";
import { useNavigate } from "react-router-dom";
import logohide from "C:\\Users\\Ratti\\myicecreamapp\\frontend\\src\\components\\hide.png"
import logoshow from "C:\\Users\\Ratti\\myicecreamapp\\frontend\\src\\components\\show.png"

const Login = () => {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [showPassword, setShowPassword] = useState(false);

    const loginclick = () => {
        alert(`Logging in as: ${username} and ${password}`);
        navigate("/home");
    };

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    return (
        <div className="login-container">
            {/* Left Section: Welcome Message */}
            <div className="welcome-section">
                <h1>WELCOME TO</h1>
                <h1 style={{marginTop: '410px'}}>ICE CREAM</h1>
                <h1>CABINET</h1>
            </div>
            {/* Right Section: Login Form */}
            <div className="login-section">
                <h2>LOGIN</h2>
                <form className="login-form">
                    <label htmlFor="username">Username</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                    <label htmlFor="password">Password</label>
                    <input
                        type={showPassword ? 'text' : 'password'}
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <></>
                    <img src={showPassword ? logoshow : logohide} 
                    style={{ width: '15px', marginTop: '-28px', marginLeft: '360px', cursor: 'pointer' }}
                    alt={showPassword ? 'Hide password' : 'Show password'}
                    onClick={togglePasswordVisibility}
                    />
                    <button 
                    type="submit" 
                    style={{fontWeight: 'lighter'}}
                    onClick={loginclick}
                    >
                    Login
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Login;