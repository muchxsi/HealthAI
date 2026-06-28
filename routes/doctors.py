from flask import Blueprint, render_template, request, redirect
from utils.roles import role_required

from models.doctor import (
get_all_doctors,
create_doctor,
get_doctor_by_id,
update_doctor,
delete_doctor,
search_doctors
)

doctors_bp = Blueprint(
"doctors",
__name__,
url_prefix="/doctors"
)

@doctors_bp.route("/")
@role_required("admin")
def list_doctors():

    keyword = request.args.get("search")

    if keyword:

        doctors = search_doctors(keyword)

    else:

        doctors = get_all_doctors()

    return render_template(
        "doctors/list.html",
        doctors=doctors
    )

@doctors_bp.route("/create", methods=["GET", "POST"])
@role_required("admin")
def create():

    if request.method == "POST":

        create_doctor(request.form)

        return redirect("/doctors/")

    return render_template(
        "doctors/create.html"
    )

@doctors_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if request.method == "POST":

        update_doctor(id, request.form)

        return redirect("/doctors/")

    doctor = get_doctor_by_id(id)

    return render_template(
        "doctors/edit.html",
        doctor=doctor
    )

@doctors_bp.route("/delete/<int:id>")
def delete(id):

    delete_doctor(id)

    return redirect("/doctors/")
