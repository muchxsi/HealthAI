from database.db import get_db


def get_all_records():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    medical_records.*,
                    patients.first_name,
                    patients.last_name
                FROM medical_records
                JOIN patients
                    ON medical_records.patient_id = patients.id
                ORDER BY medical_records.id DESC
                """
            )

            return cur.fetchall()

    finally:

        conn.close()


def get_record_by_id(record_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM medical_records
                WHERE id=%s
                """,
                (record_id,)
            )

            return cur.fetchone()

    finally:

        conn.close()


def create_record(data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO medical_records
                (
                    patient_id,
                    appointment_id,
                    diagnosis,
                    symptoms,
                    treatment,
                    prescription,
                    notes
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    data["patient_id"],
                    data["appointment_id"],
                    data["diagnosis"],
                    data["symptoms"],
                    data["treatment"],
                    data["prescription"],
                    data["notes"]
                )
            )

        conn.commit()

    finally:

        conn.close()


def update_record(record_id, data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                UPDATE medical_records
                SET
                    patient_id=%s,
                    appointment_id=%s,
                    diagnosis=%s,
                    symptoms=%s,
                    treatment=%s,
                    prescription=%s,
                    notes=%s
                WHERE id=%s
                """,
                (
                    data["patient_id"],
                    data["appointment_id"],
                    data["diagnosis"],
                    data["symptoms"],
                    data["treatment"],
                    data["prescription"],
                    data["notes"],
                    record_id
                )
            )

        conn.commit()

    finally:

        conn.close()


def delete_record(record_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM medical_records
                WHERE id=%s
                """,
                (record_id,)
            )

        conn.commit()

    finally:

        conn.close()


def search_records(keyword):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    medical_records.*,
                    patients.first_name,
                    patients.last_name
                FROM medical_records
                JOIN patients
                    ON medical_records.patient_id = patients.id
                WHERE
                    patients.first_name LIKE %s
                    OR patients.last_name LIKE %s
                    OR medical_records.diagnosis LIKE %s
                    OR medical_records.symptoms LIKE %s
                    OR medical_records.treatment LIKE %s
                ORDER BY medical_records.id DESC
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
