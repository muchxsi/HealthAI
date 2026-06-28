from flask import Flask, render_template
from flask_login import LoginManager
from dotenv import load_dotenv
import os

from database.db import get_db
from models.user import User
from models.dashboard import dashboard_stats

import routes.auth

from routes.patients import patients_bp
from routes.doctors import doctors_bp
from routes.medical_records import medical_records_bp
from routes.billing import billing_bp
from routes.pharmacy import pharmacy_bp
from routes.laboratory import laboratory_bp
from routes.ai_assistant import ai_bp
from routes.appointments import appointments_bp
from api.patients_api import patients_api_bp
from api.doctors_api import doctors_api_bp
from api.appointments_api import appointments_api_bp
from api.billing_api import billing_api_bp
from api.pharmacy_api import pharmacy_api_bp
from api.laboratory_api import laboratory_api_bp
from api.medical_records_api import medical_records_api_bp
from api.auth_api import auth_api_bp

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):

    conn = get_db()

    try:

        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM users
                WHERE id=%s
                """,
                (user_id,)
            )

            data = cur.fetchone()

            if data:
                return User(data)

            return None

    finally:

        conn.close()

# ==========================

# BLUEPRINTS

# ==========================

app.register_blueprint(routes.auth.auth_bp)

app.register_blueprint(patients_bp)

app.register_blueprint(doctors_bp)

app.register_blueprint(medical_records_bp)

app.register_blueprint(billing_bp)

app.register_blueprint(pharmacy_bp)

app.register_blueprint(laboratory_bp)

app.register_blueprint(ai_bp)

app.register_blueprint(appointments_bp)

app.register_blueprint(patients_api_bp)

app.register_blueprint(doctors_api_bp)

app.register_blueprint(appointments_api_bp)

app.register_blueprint(billing_api_bp)

app.register_blueprint(pharmacy_api_bp)

app.register_blueprint(laboratory_api_bp)

app.register_blueprint(medical_records_api_bp)

app.register_blueprint(auth_api_bp)

# ==========================

# DASHBOARD

# ==========================

@app.route("/")
@app.route("/dashboard")
def dashboard():

    stats = dashboard_stats()

    return render_template(
        "dashboard.html",
        stats=stats
)

# ==========================

# ERROR PAGES

# ==========================

@app.errorhandler(403)
def forbidden(error):

    return render_template(
        "errors/403.html"
    ), 403

@app.errorhandler(404)
def not_found(error):

    return render_template(
        "errors/404.html"
    ), 404

@app.errorhandler(500)
def server_error(error):

    return render_template(
        "errors/500.html"
    ), 500

# ==========================

# RUN APP

# ==========================

if __name__ == "__main__":

    app.run(debug=True)
