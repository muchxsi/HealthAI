import { useEffect, useState } from "react";
import ModuleLayout from "../../components/common/ModuleLayout";
import { getAppointments } from "../../services/appointmentService";

function Appointments() {

    const [appointments, setAppointments] = useState([]);

    useEffect(() => {

        getAppointments()
            .then((data) => setAppointments(data))
            .catch((err) => console.error(err));

    }, []);

    return (

        <ModuleLayout

            title="📅 Appointments"

            description="Manage hospital appointments."

            button="+ New Appointment"

            stats={[

                {
                    title: "Today's Appointments",
                    value: appointments.length
                },

                {
                    title: "Confirmed",
                    value: appointments.length
                },

                {
                    title: "Pending",
                    value: 4
                },

                {
                    title: "Completed",
                    value: 18
                }

            ]}

        >

            <div className="recent-patients">

                <table className="patients-table">

                    <thead>

                        <tr>

                            <th>Patient</th>

                            <th>Doctor</th>

                            <th>Time</th>

                        </tr>

                    </thead>

                    <tbody>

                        {appointments.map((appointment, index) => (

                            <tr key={index}>

                                <td>{appointment.patient}</td>

                                <td>{appointment.doctor}</td>

                                <td>{appointment.time}</td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </ModuleLayout>

    );

}

export default Appointments;