from flask import Blueprint, request, jsonify

from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from database.db import get_db
from models.user import User


auth_api_bp = Blueprint(
    "auth_api",
    __name__,
    url_prefix="/api/auth"
)


@auth_api_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data["username"]
    email = data["email"]
    password = data["password"]

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

    return jsonify({
        "message": "User registered successfully."
    }), 201


@auth_api_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data["email"]
    password = data["password"]

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

        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        })

    return jsonify({
        "error": "Invalid email or password"
    }), 401


@auth_api_bp.route("/me", methods=["GET"])
@login_required
def me():

    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role
    })


@auth_api_bp.route("/logout", methods=["POST"])
@login_required
def logout():

    logout_user()

    return jsonify({
        "message": "Logged out successfully."
    })