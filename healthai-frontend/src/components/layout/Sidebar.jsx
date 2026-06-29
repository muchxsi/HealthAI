import { NavLink } from "react-router-dom";

import {
    FaHospital,
    FaUserInjured,
    FaUserMd,
    FaCalendarCheck,
    FaMoneyBillWave,
    FaPills,
    FaFlask,
    FaNotesMedical,
    FaRobot
} from "react-icons/fa";

import "./sidebar.css";

function Sidebar() {

    const menu = [

        { name: "Dashboard", icon: <FaHospital />, path: "/dashboard" },

        { name: "Patients", icon: <FaUserInjured />, path: "/patients" },

        { name: "Doctors", icon: <FaUserMd />, path: "/doctors" },

        { name: "Appointments", icon: <FaCalendarCheck />, path: "/appointments" },

        { name: "Billing", icon: <FaMoneyBillWave />, path: "/billing" },

        { name: "Pharmacy", icon: <FaPills />, path: "/pharmacy" },

        { name: "Laboratory", icon: <FaFlask />, path: "/laboratory" },

        { name: "Medical Records", icon: <FaNotesMedical />, path: "/medical-records" },

        { name: "AI Assistant", icon: <FaRobot />, path: "/ai-assistant" }

    ];

    return (

        <aside className="sidebar">

            <div className="logo">

                🏥 HealthAI

            </div>

            <nav>

                {menu.map((item) => (

                    <NavLink
                        key={item.name}
                        to={item.path}
                        className="menu-item"
                    >

                        <span className="icon">
                            {item.icon}
                        </span>

                        <span>
                            {item.name}
                        </span>

                    </NavLink>

                ))}

            </nav>

            <div className="sidebar-footer">

                <div className="user-card">

                    <div className="avatar">

                        S

                    </div>

                    <div className="user-info">

                        <h4>Samuel</h4>

                        <p>Administrator</p>

                    </div>

                </div>

            </div>

        </aside>

    );

}

export default Sidebar;