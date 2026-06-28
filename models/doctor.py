from database.db import get_db


def get_all_doctors():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM doctors
                ORDER BY id DESC
                """
            )

            return cur.fetchall()

    finally:

        conn.close()


def get_doctor_by_id(doctor_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM doctors
                WHERE id=%s
                """,
                (doctor_id,)
            )

            return cur.fetchone()

    finally:

        conn.close()


def create_doctor(data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO doctors
                (
                    first_name,
                    last_name,
                    specialization,
                    department,
                    phone,
                    email,
                    consultation_fee
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    data["first_name"],
                    data["last_name"],
                    data["specialization"],
                    data["department"],
                    data["phone"],
                    data["email"],
                    data["consultation_fee"]
                )
            )

        conn.commit()

    finally:

        conn.close()


def update_doctor(doctor_id, data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                UPDATE doctors
                SET
                    first_name=%s,
                    last_name=%s,
                    specialization=%s,
                    department=%s,
                    phone=%s,
                    email=%s,
                    consultation_fee=%s
                WHERE id=%s
                """,
                (
                    data["first_name"],
                    data["last_name"],
                    data["specialization"],
                    data["department"],
                    data["phone"],
                    data["email"],
                    data["consultation_fee"],
                    doctor_id
                )
            )

        conn.commit()

    finally:

        conn.close()


def delete_doctor(doctor_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM doctors
                WHERE id=%s
                """,
                (doctor_id,)
            )

        conn.commit()

    finally:

        conn.close()


def search_doctors(keyword):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM doctors
                WHERE
                    first_name LIKE %s
                    OR last_name LIKE %s
                    OR specialization LIKE %s
                    OR department LIKE %s
                ORDER BY id DESC
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