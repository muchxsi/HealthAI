from flask import Blueprint, render_template, request, redirect

from utils.roles import role_required

from models.appointment import (
    get_all_appointments,
    create_appointment,
    get_appointment_by_id,
    update_appointment,
    delete_appointment,
    search_appointments
)

from models.patient import get_all_patients
from models.doctor import get_all_doctors


appointments_bp = Blueprint(
    "appointments",
    __name__,
    url_prefix="/appointments"
)


@appointments_bp.route("/")
@role_required("admin", "doctor", "receptionist")
def list_appointments():

    keyword = request.args.get("search")

    if keyword:

        appointments = search_appointments(keyword)

    else:

        appointments = get_all_appointments()

    return render_template(
        "appointments/list.html",
        appointments=appointments
    )


@appointments_bp.route("/create", methods=["GET", "POST"])
@role_required("admin", "receptionist")
def create():

    if request.method == "POST":

        create_appointment(request.form)

        return redirect("/appointments/")

    patients = get_all_patients()
    doctors = get_all_doctors()

    return render_template(
        "appointments/create.html",
        patients=patients,
        doctors=doctors
    )


@appointments_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@role_required("admin", "receptionist")
def edit(id):

    if request.method == "POST":

        update_appointment(id, request.form)

        return redirect("/appointments/")

    appointment = get_appointment_by_id(id)

    patients = get_all_patients()
    doctors = get_all_doctors()

    return render_template(
        "appointments/edit.html",
        appointment=appointment,
        patients=patients,
        doctors=doctors
    )


@appointments_bp.route("/delete/<int:id>")
@role_required("admin")
def delete(id):

    delete_appointment(id)

    return redirect("/appointments/")