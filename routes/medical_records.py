from flask import Blueprint, render_template, request, redirect

from utils.roles import role_required

from models.medical_record import (
    get_all_records,
    get_record_by_id,
    create_record,
    update_record,
    delete_record,
    search_records
)

from models.patient import get_all_patients
from models.appointment import get_all_appointments


medical_records_bp = Blueprint(
    "medical_records",
    __name__,
    url_prefix="/medical-records"
)


@medical_records_bp.route("/")
@role_required("admin", "doctor")
def list_records():

    keyword = request.args.get("search")

    if keyword:

        records = search_records(keyword)

    else:

        records = get_all_records()

    return render_template(
        "medical_records/list.html",
        records=records
    )


@medical_records_bp.route("/create", methods=["GET", "POST"])
@role_required("admin", "doctor")
def create():

    if request.method == "POST":

        create_record(request.form)

        return redirect("/medical-records/")

    patients = get_all_patients()
    appointments = get_all_appointments()

    return render_template(
        "medical_records/create.html",
        patients=patients,
        appointments=appointments
    )


@medical_records_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@role_required("admin", "doctor")
def edit(id):

    if request.method == "POST":

        update_record(id, request.form)

        return redirect("/medical-records/")

    record = get_record_by_id(id)

    patients = get_all_patients()
    appointments = get_all_appointments()

    return render_template(
        "medical_records/edit.html",
        record=record,
        patients=patients,
        appointments=appointments
    )


@medical_records_bp.route("/delete/<int:id>")
@role_required("admin")
def delete(id):

    delete_record(id)

    return redirect("/medical-records/")