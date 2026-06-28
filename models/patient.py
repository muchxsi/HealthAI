from database.db import get_db

def get_all_patients():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                "SELECT * FROM patients ORDER BY id DESC"
            )

            return cur.fetchall()

    finally:

        conn.close()

def create_patient(data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO patients
                (
                    first_name,
                    last_name,
                    gender,
                    phone,
                    email,
                    dob,
                    address
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    data["first_name"],
                    data["last_name"],
                    data["gender"],
                    data["phone"],
                    data["email"],
                    data["dob"],
                    data["address"]
                )
            )

        conn.commit()

    finally:

        conn.close()

def get_patient_by_id(patient_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM patients
                WHERE id=%s
                """,
                (patient_id,)
            )

            return cur.fetchone()

    finally:

        conn.close()

def update_patient(patient_id, data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                UPDATE patients
                SET
                    first_name=%s,
                    last_name=%s,
                    gender=%s,
                    phone=%s,
                    email=%s,
                    dob=%s,
                    address=%s
                WHERE id=%s
                """,
                (
                    data["first_name"],
                    data["last_name"],
                    data["gender"],
                    data["phone"],
                    data["email"],
                    data["dob"],
                    data["address"],
                    patient_id
                )
            )

        conn.commit()

    finally:

        conn.close()

def delete_patient(patient_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM patients
                WHERE id=%s
                """,
                (patient_id,)
            )

        conn.commit()

    finally:

        conn.close()

def search_patients(keyword):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM patients
                WHERE
                    first_name LIKE %s
                    OR last_name LIKE %s
                    OR phone LIKE %s
                ORDER BY id DESC
                """,
                (
                    f"%{keyword}%",
                    f"%{keyword}%",
                    f"%{keyword}%"
                )
            )

            return cur.fetchall()

    finally:

        conn.close()
