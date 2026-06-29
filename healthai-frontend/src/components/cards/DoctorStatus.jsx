function DoctorStatus() {

    const doctors = [

        {
            name: "Dr. Sarah",
            status: "Available"
        },

        {
            name: "Dr. James",
            status: "In Surgery"
        },

        {
            name: "Dr. Mercy",
            status: "Offline"
        }

    ];

    return (

        <div className="recent-patients">

            <h3>Doctor Status</h3>

            <table className="patients-table">

                <thead>

                    <tr>

                        <th>Doctor</th>

                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    {doctors.map((doctor, index) => (

                        <tr key={index}>

                            <td>{doctor.name}</td>

                            <td>{doctor.status}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default DoctorStatus;