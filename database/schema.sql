CREATE TABLE IF NOT EXISTS users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(100) UNIQUE NOT NULL,

    email VARCHAR(120) UNIQUE NOT NULL,

    password_hash TEXT NOT NULL,

    role ENUM(
        'admin',
        'doctor',
        'receptionist',
        'pharmacist',
        'lab_technician'
    ) DEFAULT 'receptionist',

    created_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP
);