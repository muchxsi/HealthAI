from flask import (
Blueprint,
render_template,
request,
redirect,
flash
)

from flask_login import (
login_user,
logout_user,
login_required
)

from werkzeug.security import (
generate_password_hash,
check_password_hash
)

from database.db import get_db
from models.user import User

auth_bp = Blueprint(
"auth",
__name__,
url_prefix="/auth"
)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        password_hash = generate_password_hash(password)

        conn = get_db()

        try:

            with conn.cursor() as cur:

                cur.execute(
                    """
                    INSERT INTO users
                    (
                        username,
                        email,
                        password_hash
                    )
                    VALUES
                    (%s,%s,%s)
                    """,
                    (
                        username,
                        email,
                        password_hash
                    )
                )

            conn.commit()

        finally:

            conn.close()

        flash(
            "Account created successfully.",
            "success"
        )

        return redirect("/auth/login")

    return render_template(
        "auth/register.html"
    )

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()

        try:

            with conn.cursor() as cur:

                cur.execute(
                    """
                    SELECT *
                    FROM users
                    WHERE email=%s
                    """,
                    (email,)
                )

                user_data = cur.fetchone()

        finally:

            conn.close()

        if user_data and check_password_hash(
            user_data["password_hash"],
            password
        ):

            user = User(user_data)

            login_user(user)

            return redirect("/dashboard")

        flash(
            "Invalid email or password.",
            "danger"
        )

    return render_template(
        "auth/login.html"
    )

@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect("/auth/login")
