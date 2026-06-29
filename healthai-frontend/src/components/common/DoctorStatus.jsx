import "./doctorStatus.css";

function DoctorStatus(){

    const doctors=[

        {
            name:"Dr. Sarah",
            status:"Available"
        },

        {
            name:"Dr. James",
            status:"In Surgery"
        },

        {
            name:"Dr. Mercy",
            status:"Consulting"
        },

        {
            name:"Dr. Peter",
            status:"Available"
        }

    ];

    return(

        <div className="doctor-card">

            <h3>Doctors On Duty</h3>

            {

                doctors.map((doctor,index)=>(

                    <div
                        className="doctor-row"
                        key={index}
                    >

                        <span>

                            {doctor.name}

                        </span>

                        <span>

                            {doctor.status}

                        </span>

                    </div>

                ))

            }

        </div>

    );

}

export default DoctorStatus;