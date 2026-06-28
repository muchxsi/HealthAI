from database.db import get_db

def get_all_bills():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    billing.*,
                    patients.first_name,
                    patients.last_name
                FROM billing
                JOIN patients
                    ON billing.patient_id = patients.id
                ORDER BY billing.id DESC
                """
            )

            return cur.fetchall()

    finally:

        conn.close()

def create_bill(data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO billing
                (
                    patient_id,
                    amount,
                    service,
                    payment_status
                )
                VALUES
                (%s,%s,%s,%s)
                """,
                (
                    data["patient_id"],
                    data["amount"],
                    data["service"],
                    data["payment_status"]
                )
            )

        conn.commit()

    finally:

        conn.close()

def get_bill_by_id(bill_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM billing
                WHERE id=%s
                """,
                (bill_id,)
            )

            return cur.fetchone()

    finally:

        conn.close()

def update_bill(bill_id, data):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                UPDATE billing
                SET
                    patient_id=%s,
                    amount=%s,
                    service=%s,
                    payment_status=%s
                WHERE id=%s
                """,
                (
                    data["patient_id"],
                    data["amount"],
                    data["service"],
                    data["payment_status"],
                    bill_id
                )
            )

        conn.commit()

    finally:

        conn.close()

def delete_bill(bill_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM billing
                WHERE id=%s
                """,
                (bill_id,)
            )

        conn.commit()

    finally:

        conn.close()

def search_bills(keyword):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    billing.*,
                    patients.first_name,
                    patients.last_name
                FROM billing
                JOIN patients
                    ON billing.patient_id = patients.id
                WHERE
                    patients.first_name LIKE %s
                    OR patients.last_name LIKE %s
                    OR billing.service LIKE %s
                    OR billing.payment_status LIKE %s
                ORDER BY billing.id DESC
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

def get_total_revenue():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT
                    COALESCE(SUM(amount),0) AS revenue
                FROM billing
                WHERE payment_status='Paid'
                """
            )

            result = cur.fetchone()

            return result["revenue"]

    finally:

        conn.close()
