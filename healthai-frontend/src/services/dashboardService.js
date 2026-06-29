import api from "./api";

export const getDashboardStats = async () => {

    const patients = await api.get("/patients");

    const doctors = await api.get("/doctors");

    const appointments = await api.get("/appointments");

    const billing = await api.get("/billing");

    return {

        patients: patients.data,

        doctors: doctors.data,

        appointments: appointments.data,

        billing: billing.data

    };

};