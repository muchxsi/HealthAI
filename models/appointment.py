from database.db import get_db

def get_all_appointments():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    appointments.id,
                    appointments.patient_id,
                    appointments.doctor_id,
                    appointments.appointment_date,
                    appointments.appointment_time,
                    appointments.status,
                    appointments.notes,
                    patients.first_name AS patient_first_name,
                    patients.last_name AS patient_last_name,
                    doctors.first_name AS doctor_first_name,
                    doctors.last_name AS doctor_last_name
                FROM appointments
                JOIN patients
                    ON appointments.patient_id = patients.id
                JOIN doctors
                    ON appointments.doctor_id = doctors.id
                ORDER BY
                    appointments.appointment_date DESC,
                    appointments.appointment_time DESC
                """
            )

            return cur.fetchall()

    finally:

        conn.close()

def create_appointment(data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO appointments
                (
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    notes
                )
                VALUES
                (%s,%s,%s,%s,%s)
                """,
                (
                    data["patient_id"],
                    data["doctor_id"],
                    data["appointment_date"],
                    data["appointment_time"],
                    data["notes"]
                )
            )

        conn.commit()

    finally:

        conn.close()

def get_appointment_by_id(appointment_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM appointments
                WHERE id=%s
                """,
                (appointment_id,)
            )

            return cur.fetchone()

    finally:

        conn.close()

def update_appointment(appointment_id, data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                UPDATE appointments
                SET
                    patient_id=%s,
                    doctor_id=%s,
                    appointment_date=%s,
                    appointment_time=%s,
                    status=%s,
                    notes=%s
                WHERE id=%s
                """,
                (
                    data["patient_id"],
                    data["doctor_id"],
                    data["appointment_date"],
                    data["appointment_time"],
                    data["status"],
                    data["notes"],
                    appointment_id
                )
            )

        conn.commit()

    finally:

        conn.close()

def delete_appointment(appointment_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM appointments
                WHERE id=%s
                """,
                (appointment_id,)
            )

        conn.commit()

    finally:

        conn.close()

def search_appointments(keyword):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    appointments.id,
                    appointments.patient_id,
                    appointments.doctor_id,
                    appointments.appointment_date,
                    appointments.appointment_time,
                    appointments.status,
                    appointments.notes,
                    patients.first_name AS patient_first_name,
                    patients.last_name AS patient_last_name,
                    doctors.first_name AS doctor_first_name,
                    doctors.last_name AS doctor_last_name
                FROM appointments
                JOIN patients
                    ON appointments.patient_id = patients.id
                JOIN doctors
                    ON appointments.doctor_id = doctors.id
                WHERE
                    patients.first_name LIKE %s
                    OR patients.last_name LIKE %s
                    OR doctors.first_name LIKE %s
                    OR doctors.last_name LIKE %s
                    OR appointments.status LIKE %s
                ORDER BY appointments.id DESC
                """,
                (
                    f"%{keyword}%",
                    f"%{keyword}%",
                    f"%{keyword}%",
                    f"%{keyword}%",
                    f"%{keyword}%"
                )
            )

            return cur.fetchall()

    finally:

        conn.close()
