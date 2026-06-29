import { useNavigate } from "react-router-dom";

function Login() {

    const navigate = useNavigate();

    const login = () => {

        localStorage.setItem("healthai-user", "Samuel");

        navigate("/dashboard");

    };

    return (

        <div style={{
            height:"100vh",
            display:"flex",
            justifyContent:"center",
            alignItems:"center",
            background:"#07121f"
        }}>

            <div style={{
                width:"400px",
                background:"white",
                padding:"40px",
                borderRadius:"20px"
            }}>

                <h1>🏥 HealthAI</h1>

                <input
                    placeholder="Email"
                    style={{width:"100%",padding:"12px",marginTop:"20px"}}
                />

                <input
                    type="password"
                    placeholder="Password"
                    style={{width:"100%",padding:"12px",marginTop:"15px"}}
                />

                <button
                    onClick={login}
                    style={{
                        width:"100%",
                        padding:"14px",
                        marginTop:"20px",
                        background:"#2563eb",
                        color:"white",
                        border:"none",
                        borderRadius:"10px",
                        cursor:"pointer"
                    }}
                >
                    Login
                </button>

            </div>

        </div>

    );

}

export default Login;