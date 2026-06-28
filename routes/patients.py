from flask import Blueprint, render_template, request, redirect
from utils.roles import role_required

from models.patient import (
get_all_patients,
create_patient,
get_patient_by_id,
update_patient,
delete_patient,
search_patients
)

patients_bp = Blueprint(
"patients",
__name__,
url_prefix="/patients"
)

@patients_bp.route("/")
@role_required("admin", "doctor", "receptionist")
def list_patients():

    keyword = request.args.get("search")

    if keyword:

        patients = search_patients(keyword)

    else:

        patients = get_all_patients()

    return render_template(
        "patients/list.html",
        patients=patients
    )

@patients_bp.route("/create", methods=["GET", "POST"])
@role_required("admin", "receptionist")
def create():

    if request.method == "POST":

        create_patient(request.form)

        return redirect("/patients/")

    return render_template(
        "patients/create.html"
    )

@patients_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    if request.method == "POST":

        update_patient(id, request.form)

        return redirect("/patients/")

    patient = get_patient_by_id(id)

    return render_template(
        "patients/edit.html",
        patient=patient
    )

@patients_bp.route("/delete/<int:id>")
def delete(id):

    delete_patient(id)

    return redirect("/patients/")
