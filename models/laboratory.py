from database.db import get_db

def get_all_tests():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    laboratory.*,
                    patients.first_name,
                    patients.last_name
                FROM laboratory
                JOIN patients
                    ON laboratory.patient_id = patients.id
                ORDER BY laboratory.id DESC
                """
            )

            return cur.fetchall()

    finally:

        conn.close()

def create_test(data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO laboratory
                (
                    patient_id,
                    test_name,
                    test_result,
                    status
                )
                VALUES
                (%s,%s,%s,%s)
                """,
                (
                    data["patient_id"],
                    data["test_name"],
                    data["test_result"],
                    data["status"]
                )
            )

        conn.commit()

    finally:

        conn.close()

def get_test_by_id(test_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM laboratory
                WHERE id=%s
                """,
                (test_id,)
            )

            return cur.fetchone()

    finally:

        conn.close()

def update_test(test_id, data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                UPDATE laboratory
                SET
                    patient_id=%s,
                    test_name=%s,
                    test_result=%s,
                    status=%s
                WHERE id=%s
                """,
                (
                    data["patient_id"],
                    data["test_name"],
                    data["test_result"],
                    data["status"],
                    test_id
                )
            )

        conn.commit()

    finally:

        conn.close()

def delete_test(test_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM laboratory
                WHERE id=%s
                """,
                (test_id,)
            )

        conn.commit()

    finally:

        conn.close()

def search_tests(keyword):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    laboratory.*,
                    patients.first_name,
                    patients.last_name
                FROM laboratory
                JOIN patients
                    ON laboratory.patient_id = patients.id
                WHERE
                    patients.first_name LIKE %s
                    OR patients.last_name LIKE %s
                    OR laboratory.test_name LIKE %s
                    OR laboratory.status LIKE %s
                ORDER BY laboratory.id DESC
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
