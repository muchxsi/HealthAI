import { Navigate, Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";
import "./layout.css";

function Layout() {

    const user = localStorage.getItem("healthai-user");

    if (!user) {

        return <Navigate to="/" replace />;

    }

    return (

        <div className="layout">

            <Sidebar />

            <div className="main-content">

                <Navbar />

                <div className="page-content">

                    <Outlet />

                </div>

            </div>

        </div>

    );

}

export default Layout;