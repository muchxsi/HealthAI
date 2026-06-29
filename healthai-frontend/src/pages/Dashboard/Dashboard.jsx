import { useEffect, useState } from "react";

import PatientChart from "../../components/charts/PatientChart";

import { getPatients } from "../../services/patientService";

import AppointmentTable from "../../components/tables/AppointmentTable";

import DoctorStatus from "../../components/cards/DoctorStatus";

import {

    FaUserInjured,

    FaUserMd,

    FaCalendarAlt,

    FaMoneyBillWave,

    FaArrowUp,

    FaPlusCircle

} from "react-icons/fa";

import "./dashboard.css";

function Dashboard() {

    const [patients, setPatients] = useState([]);

    useEffect(() => {

        loadPatients();

    }, []);

    const loadPatients = async () => {

        try {

            const data = await getPatients();

            setPatients(data);

        } catch (error) {

            console.error(error);

        }

    };

    const stats = [

        {
            title: "Patients",
            value: patients.length,
            value: "1,248",
            icon: <FaUserInjured />,
            color: "#2563eb"
        },

        {
            title: "Doctors",
            value: "82",
            icon: <FaUserMd />,
            color: "#16a34a"
        },

        {
            title: "Appointments",
            value: "320",
            icon: <FaCalendarAlt />,
            color: "#9333ea"
        },

        {
            title: "Revenue",
            value: "KSh 2.4M",
            icon: <FaMoneyBillWave />,
            color: "#f59e0b"
        }

    ];

    return (

        <>

            <div className="hero">

                <div>

                    <h1>

                        Welcome back,
                        <span> Samuel 👋</span>

                    </h1>

                    <p>

                        Here's today's hospital overview.

                    </p>

                </div>

                <button className="new-btn">

                    <FaPlusCircle />

                    New Patient

                </button>

            </div>

            <div className="cards">

                {stats.map((card) => (

                    <div
                        className="card-box"
                        key={card.title}
                    >

                        <div
                            className="icon-circle"
                            style={{
                                background: card.color
                            }}
                        >

                            {card.icon}

                        </div>

                        <h3>

                            {card.title}

                        </h3>

                        <h1>

                            {card.value}

                        </h1>

                        <small>

                            <FaArrowUp />

                            12% this month

                        </small>

                    </div>

                ))}

            </div>

            <div className="dashboard-grid">

                <div className="activity">

                    <h3>

                        Recent Activity

                    </h3>

                    <ul>

                        <li>✔ John Mwangi checked in</li>

                        <li>✔ Lab results uploaded</li>

                        <li>✔ Pharmacy issued medication</li>

                        <li>✔ Appointment confirmed</li>

                    </ul>

                </div>

                <div className="status">

                    <h3>

                        Hospital Status

                    </h3>

                    <h1>

                        🟢 Operational

                    </h1>

                    <p>

                        All hospital services are running normally.

                    </p>

                </div>

            </div>
            <PatientChart />
            <AppointmentTable />
            <DoctorStatus />
            {/* <NotificationPanel /> */}

            <div className="performance">

                <h3>🏥 Hospital Performance</h3>

                <div className="progress-item">

                    <div className="progress-header">
                        <span>Bed Occupancy</span>
                        <span>81%</span>
                    </div>

                    <div className="progress-bar">

                        <div
                            className="progress-fill blue"
                            style={{ width: "81%" }}
                        ></div>

                    </div>

                </div>

                <div className="progress-item">

                    <div className="progress-header">
                        <span>Doctors Available</span>
                        <span>92%</span>
                    </div>

                    <div className="progress-bar">

                        <div
                            className="progress-fill green"
                            style={{ width: "92%" }}
                        ></div>

                    </div>

                </div>

                <div className="progress-item">

                    <div className="progress-header">
                        <span>Revenue Target</span>
                        <span>68%</span>
                    </div>

                    <div className="progress-bar">

                        <div
                            className="progress-fill orange"
                            style={{ width: "68%" }}
                        ></div>

                    </div>

                </div>

                <div className="progress-item">

                    <div className="progress-header">
                        <span>Patient Satisfaction</span>
                        <span>97%</span>
                    </div>

                    <div className="progress-bar">

                        <div
                            className="progress-fill purple"
                            style={{ width: "97%" }}
                        ></div>

                    </div>

                </div>

            </div>

            <div className="recent-patients">

                <h3>Recent Patients</h3>

                <table className="patients-table">

                    <thead>

                        <tr>

                            <th>ID</th>

                            <th>Name</th>

                            <th>Gender</th>

                            <th>Phone</th>

                        </tr>

                    </thead>

                    <tbody>

                        {patients.slice(0, 5).map((patient) => (

                            <tr key={patient.id}>

                                <td>{patient.id}</td>

                                <td>
                                    {patient.first_name} {patient.last_name}
                                </td>

                                <td>{patient.gender}</td>

                                <td>{patient.phone}</td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </>

    );

}

export default Dashboard;