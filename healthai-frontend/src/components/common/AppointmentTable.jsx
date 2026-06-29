import "./appointmentTable.css";

function AppointmentTable() {

    const appointments = [

        {
            patient:"John Mwangi",
            doctor:"Dr. Sarah",
            time:"08:30 AM",
            status:"Completed"
        },

        {
            patient:"Grace Wanjiku",
            doctor:"Dr. James",
            time:"10:00 AM",
            status:"Waiting"
        },

        {
            patient:"Kevin Otieno",
            doctor:"Dr. Mercy",
            time:"11:30 AM",
            status:"In Progress"
        },

        {
            patient:"Faith Akinyi",
            doctor:"Dr. Peter",
            time:"02:00 PM",
            status:"Scheduled"
        }

    ];

    const badgeClass = (status) => {

        switch(status){

            case "Completed":
                return "badge completed";

            case "Waiting":
                return "badge waiting";

            case "In Progress":
                return "badge progress";

            default:
                return "badge scheduled";

        }

    };

    return (

        <div className="appointments-card">

            <div className="table-header">

                <h3>Today's Appointments</h3>

            </div>

            <table>

                <thead>

                    <tr>

                        <th>Patient</th>

                        <th>Doctor</th>

                        <th>Time</th>

                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    {appointments.map((item,index)=>(

                        <tr key={index}>

                            <td>{item.patient}</td>

                            <td>{item.doctor}</td>

                            <td>{item.time}</td>

                            <td>

                                <span className={badgeClass(item.status)}>

                                    {item.status}

                                </span>

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default AppointmentTable;