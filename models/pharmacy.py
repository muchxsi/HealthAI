from database.db import get_db

def get_all_medications():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    pharmacy.*,
                    patients.first_name,
                    patients.last_name
                FROM pharmacy
                JOIN patients
                    ON pharmacy.patient_id = patients.id
                ORDER BY pharmacy.id DESC
                """
            )

            return cur.fetchall()

    finally:

        conn.close()

def create_medication(data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO pharmacy
                (
                    patient_id,
                    medication_name,
                    dosage,
                    quantity,
                    status
                )
                VALUES
                (%s,%s,%s,%s,%s)
                """,
                (
                    data["patient_id"],
                    data["medication_name"],
                    data["dosage"],
                    data["quantity"],
                    data["status"]
                )
            )

        conn.commit()

    finally:

        conn.close()

def get_medication_by_id(medication_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM pharmacy
                WHERE id=%s
                """,
                (medication_id,)
            )

            return cur.fetchone()

    finally:

        conn.close()

def update_medication(medication_id, data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                UPDATE pharmacy
                SET
                    patient_id=%s,
                    medication_name=%s,
                    dosage=%s,
                    quantity=%s,
                    status=%s
                WHERE id=%s
                """,
                (
                    data["patient_id"],
                    data["medication_name"],
                    data["dosage"],
                    data["quantity"],
                    data["status"],
                    medication_id
                )
            )

        conn.commit()

    finally:

        conn.close()

def delete_medication(medication_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM pharmacy
                WHERE id=%s
                """,
                (medication_id,)
            )

        conn.commit()

    finally:

        conn.close()

def search_medications(keyword):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    pharmacy.*,
                    patients.first_name,
                    patients.last_name
                FROM pharmacy
                JOIN patients
                    ON pharmacy.patient_id = patients.id
                WHERE
                    patients.first_name LIKE %s
                    OR patients.last_name LIKE %s
                    OR pharmacy.medication_name LIKE %s
                    OR pharmacy.status LIKE %s
                ORDER BY pharmacy.id DESC
                """,
                (
                    f"%{keyword}%",
                    f"%{keyword}%",
                    f"%{keyword}%",
                    f"%{keyword}%"
                )
            )

            return cur.fetchall()

    finally:

        conn.close()
