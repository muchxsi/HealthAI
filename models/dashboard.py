from database.db import get_db

def dashboard_stats():

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                "SELECT COUNT(*) AS total FROM patients"
            )
            patients = cur.fetchone()["total"]

            cur.execute(
                "SELECT COUNT(*) AS total FROM doctors"
            )
            doctors = cur.fetchone()["total"]

            cur.execute(
                "SELECT COUNT(*) AS total FROM appointments"
            )
            appointments = cur.fetchone()["total"]

            cur.execute(
                """
                SELECT COUNT(*) AS total
                FROM billing
                WHERE payment_status='Pending'
                """
            )
            pending_bills = cur.fetchone()["total"]

            cur.execute(
                """
                SELECT COUNT(*) AS total
                FROM laboratory
                WHERE status='Pending'
                """
            )
            pending_tests = cur.fetchone()["total"]

            cur.execute(
                """
                SELECT COALESCE(SUM(amount),0) AS revenue
                FROM billing
                WHERE payment_status='Paid'
                """
            )
            revenue = cur.fetchone()["revenue"]

            cur.execute(
                """
                SELECT *
                FROM patients
                ORDER BY id DESC
                LIMIT 5
                """
            )
            recent_patients = cur.fetchall()

            cur.execute(
                """
                SELECT *
                FROM appointments
                ORDER BY id DESC
                LIMIT 5
                """
            )
            recent_appointments = cur.fetchall()

        return {

            "patients": patients,

            "doctors": doctors,

            "appointments": appointments,

            "pending_bills": pending_bills,

            "pending_tests": pending_tests,

            "revenue": revenue,

            "recent_patients": recent_patients,

            "recent_appointments": recent_appointments
        }

    finally:

        conn.close()
