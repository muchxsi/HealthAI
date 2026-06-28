# 🏥 HealthAI

An AI-Powered Hospital Management System built with **Flask**, **MySQL**, and a modern REST API architecture.

HealthAI is designed to help hospitals manage patients, doctors, appointments, billing, pharmacy, laboratory services, and medical records from a centralized platform.

---

# 🚀 Features

## Authentication

- User Registration
- User Login
- Secure Password Hashing
- Role-Based Access Control
- Session Management

---

## Dashboard

- Total Patients
- Total Doctors
- Total Appointments
- Revenue Statistics
- Pending Bills
- Pending Laboratory Tests
- Recent Patients
- Recent Appointments

---

## Patient Management

- Add Patient
- Edit Patient
- Delete Patient
- Search Patients

---

## Doctor Management

- Add Doctor
- Edit Doctor
- Delete Doctor
- Search Doctors

---

## Appointment Management

- Schedule Appointments
- Update Appointments
- Cancel Appointments
- Search Appointments

---

## Medical Records

- Diagnosis
- Symptoms
- Treatment
- Prescription
- Doctor Notes

---

## Billing

- Create Bills
- Payment Status
- Revenue Tracking

---

## Pharmacy

- Medication Management
- Dispensing Status

---

## Laboratory

- Laboratory Tests
- Test Results
- Pending Tests

---

## AI Assistant

- AI Healthcare Assistant
- REST API Ready

---

# 🔐 User Roles

- Administrator
- Doctor
- Receptionist
- Pharmacist
- Laboratory Technician

---

# 🛠 Technology Stack

## Backend

- Python
- Flask
- Flask-Login
- PyMySQL
- MySQL

## Frontend (Current)

- HTML
- Bootstrap 5
- Jinja2

## Frontend (Upcoming)

- React
- Vite
- Axios
- React Router
- Chart.js

---

# 📁 Project Structure


HealthAI/
│
├── api/
├── database/
├── models/
├── routes/
├── static/
├── templates/
├── uploads/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .env.example
└── README.md


---

# ⚙ Installation

## Clone Repository

bash
git clone https://github.com/YOUR_USERNAME/HealthAI.git


---

## Create Virtual Environment

bash
python -m venv .venv


---

## Activate Environment

Windows

bash
.venv\Scripts\activate


Linux/macOS

bash
source .venv/bin/activate


---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example:

env
SECRET_KEY=your-secret-key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your-password
MYSQL_DATABASE=healthai


---

## Run Application

bash
python app.py


---

# 🌐 REST API

Patients


GET     /api/patients/
POST    /api/patients/
PUT     /api/patients/<id>
DELETE  /api/patients/<id>


Doctors


GET     /api/doctors/
POST    /api/doctors/
PUT     /api/doctors/<id>
DELETE  /api/doctors/<id>


Appointments


GET     /api/appointments/
POST    /api/appointments/
PUT     /api/appointments/<id>
DELETE  /api/appointments/<id>


Billing


GET     /api/billing/
POST    /api/billing/
PUT     /api/billing/<id>
DELETE  /api/billing/<id>


Pharmacy


GET     /api/pharmacy/
POST    /api/pharmacy/
PUT     /api/pharmacy/<id>
DELETE  /api/pharmacy/<id>


Laboratory


GET     /api/laboratory/
POST    /api/laboratory/
PUT     /api/laboratory/<id>
DELETE  /api/laboratory/<id>


Medical Records


GET     /api/medical-records/
POST    /api/medical-records/
PUT     /api/medical-records/<id>
DELETE  /api/medical-records/<id>


# 🚧 Roadmap

- React Frontend
- Docker Support
- CI/CD Pipeline
- AI Symptom Checker
- AI Appointment Prediction
- SMS Notifications
- Email Notifications
- File Uploads
- Audit Logs
- Multi-Hospital Support

---

# 📌 Version

Current Release

HealthAI Backend v1.0


---

# 👨‍💻 Author

**Samuel Muchasi**

- GitHub: https://github.com/muchxsi

---

# 📄 License

This project is licensed under the MIT License.