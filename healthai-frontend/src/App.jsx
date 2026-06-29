import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/layout/Layout";

import Dashboard from "./pages/Dashboard/Dashboard";
import Login from "./pages/Login/Login";
import Patients from "./pages/Patients/Patients";
import Doctors from "./pages/Doctors/Doctors";
import Appointments from "./pages/Appointments/Appointments";
import Billing from "./pages/Billing/Billing";
import Pharmacy from "./pages/Pharmacy/Pharmacy";
import Laboratory from "./pages/Laboratory/Laboratory";
import MedicalRecords from "./pages/MedicalRecords/MedicalRecords";
import AIAssistant from "./pages/AIAssistant/AIAssistant";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Login />} />

        <Route element={<Layout />}>

          <Route path="/dashboard" element={<Dashboard />} />

          <Route path="/patients" element={<Patients />} />

          <Route path="/doctors" element={<Doctors />} />

          <Route path="/appointments" element={<Appointments />} />

          <Route path="/billing" element={<Billing />} />

          <Route path="/pharmacy" element={<Pharmacy />} />

          <Route path="/laboratory" element={<Laboratory />} />

          <Route path="/medical-records" element={<MedicalRecords />} />

          <Route path="/ai-assistant" element={<AIAssistant />} />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;