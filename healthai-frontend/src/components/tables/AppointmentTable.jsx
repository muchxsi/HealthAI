function AppointmentTable() {
  const appointments = [
    {
      patient: "John Mwangi",
      doctor: "Dr. Sarah",
      time: "09:00 AM",
      status: "Confirmed",
    },
    {
      patient: "Grace Wanjiku",
      doctor: "Dr. James",
      time: "10:30 AM",
      status: "Waiting",
    },
    {
      patient: "Peter Otieno",
      doctor: "Dr. Mercy",
      time: "11:15 AM",
      status: "Completed",
    },
  ];

  return (
    <div className="recent-patients">
      <h3>Today's Appointments</h3>

      <table className="patients-table">
        <thead>
          <tr>
            <th>Patient</th>
            <th>Doctor</th>
            <th>Time</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {appointments.map((appointment, index) => (
            <tr key={index}>
              <td>{appointment.patient}</td>
              <td>{appointment.doctor}</td>
              <td>{appointment.time}</td>
              <td>{appointment.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AppointmentTable;