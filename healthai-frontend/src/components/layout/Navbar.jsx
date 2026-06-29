import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
    FaBell,
    FaSearch,
    FaUserCircle
} from "react-icons/fa";

import "./navbar.css";

function Navbar() {

    const navigate = useNavigate();

    const user = localStorage.getItem("healthai-user") || "Administrator";

    const logout = () => {

        localStorage.removeItem("healthai-user");

        navigate("/");

    };

    const [time, setTime] = useState("");

    useEffect(() => {

        const updateClock = () => {

            const now = new Date();

            setTime(

                now.toLocaleTimeString("en-GB", {

                    hour: "2-digit",
                    minute: "2-digit",
                    second: "2-digit"

                })

            );

        };

        updateClock();

        const timer = setInterval(updateClock, 1000);

        return () => clearInterval(timer);

    }, []);

    const today = new Date().toLocaleDateString("en-GB", {

        weekday: "long",
        day: "numeric",
        month: "long",
        year: "numeric"

    });

    return (

        <header className="navbar">

            <div className="navbar-left">

                <h2>

                    Welcome back, {user} 👋

                </h2>

                <div className="date-time">

                    <p>{today}</p>

                    <h3>{time}</h3>

                </div>

            </div>

            <div className="navbar-right">

                <div className="search-box">

                    <FaSearch />

                    <input

                        type="text"

                        placeholder="Search patients, doctors..."

                    />

                </div>

                <div className="notification">

                    <button className="icon-btn">

                        <FaBell />

                    </button>

                    <span className="badge">

                        3

                    </span>

                </div>

                <div className="profile">

                    <FaUserCircle
                        size={38}
                        color="#ffffff"
                    />

                    <div className="user-info">

                        <h4>{user}</h4>

                        <p>Administrator</p>

                    </div>

                    <button

                        className="logout-btn"

                        onClick={logout}

                    >

                        Logout

                    </button>

                </div>

            </div>

        </header>

    );

}

export default Navbar;