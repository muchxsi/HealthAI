import { FaBell } from "react-icons/fa";
import "./notification.css";

function NotificationPanel() {

    const notifications = [

        "🚑 Emergency patient admitted",

        "💊 Pharmacy stock updated",

        "🧪 Lab results available",

        "📅 12 appointments today",

        "👨‍⚕️ Dr. Mercy is now online"

    ];

    return (

        <div className="notify-card">

            <h3>

                <FaBell />

                Notifications

            </h3>

            {notifications.map((item,index)=>(

                <div
                    className="notify-item"
                    key={index}
                >

                    {item}

                </div>

            ))}

        </div>

    );

}

export default NotificationPanel;