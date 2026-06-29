import {
    Line
} from "react-chartjs-2";

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend,
    Filler
} from "chart.js";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend,
    Filler
);

function PatientChart() {

    const data = {

        labels: [

            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"

        ],

        datasets: [

            {

                label: "Patients",

                data: [

                    180,
                    250,
                    300,
                    420,
                    510,
                    690

                ],

                borderColor: "#2563eb",

                backgroundColor: "rgba(37,99,235,.15)",

                fill: true,

                tension: .4

            }

        ]

    };

    const options = {

        responsive: true,

        plugins: {

            legend: {

                display: false

            }

        },

        scales: {

            x: {

                ticks: {

                    color: "#c9d4e3"

                },

                grid: {

                    color: "rgba(255,255,255,.05)"

                }

            },

            y: {

                ticks: {

                    color: "#c9d4e3"

                },

                grid: {

                    color: "rgba(255,255,255,.05)"

                }

            }

        }

    };

    return (

        <div
            style={{
                background:"#10243d",
                padding:"25px",
                borderRadius:"20px",
                marginTop:"30px"
            }}
        >

            <h4
                style={{
                    color:"white",
                    marginBottom:"20px"
                }}
            >

                Patient Analytics

            </h4>

            <Line
                data={data}
                options={options}
            />

        </div>

    );

}

export default PatientChart;