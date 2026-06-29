import { useEffect, useState } from "react";
import ModuleLayout from "../../components/common/ModuleLayout";
import { getDoctors } from "../../services/doctorService";

function Doctors() {

    const [doctors, setDoctors] = useState([]);

    useEffect(() => {

        getDoctors()
            .then((data) => setDoctors(data))
            .catch((err) => console.error(err));

    }, []);

    return (

        <ModuleLayout

            title="👨‍⚕️ Doctors"

            description="Manage doctors, specialties and hospital schedules."

            button="+ Add Doctor"

            stats={[

                {
                    title: "Doctors",
                    value: doctors.length
                },

                {
                    title: "Available",
                    value: doctors.length
                },

                {
                    title: "Departments",
                    value: 12
                },

                {
                    title: "On Duty",
                    value: doctors.length
                }

            ]}

        >

            <div className="recent-patients">

                <table className="patients-table">

                    <thead>

                        <tr>

                            <th>ID</th>

                            <th>Name</th>

                            <th>Specialty</th>

                        </tr>

                    </thead>

                    <tbody>

                        {doctors.map((doctor) => (

                            <tr key={doctor.id}>

                                <td>{doctor.id}</td>

                                <td>{doctor.name}</td>

                                <td>{doctor.specialty}</td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </ModuleLayout>

    );

}

export default Doctors;