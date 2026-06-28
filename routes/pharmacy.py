from flask import Blueprint, render_template, request, redirect

from utils.roles import role_required

from models.pharmacy import (
    get_all_medications,
    create_medication,
    get_medication_by_id,
    update_medication,
    delete_medication,
    search_medications
)

from models.patient import get_all_patients


pharmacy_bp = Blueprint(
    "pharmacy",
    __name__,
    url_prefix="/pharmacy"
)


@pharmacy_bp.route("/")
@role_required("admin", "pharmacist")
def list_medications():

    keyword = request.args.get("search")

    if keyword:

        medications = search_medications(keyword)

    else:

        medications = get_all_medications()

    return render_template(
        "pharmacy/list.html",
        medications=medications
    )


@pharmacy_bp.route("/create", methods=["GET", "POST"])
@role_required("admin", "pharmacist")
def create():

    if request.method == "POST":

        create_medication(request.form)

        return redirect("/pharmacy/")

    patients = get_all_patients()

    return render_template(
        "pharmacy/create.html",
        patients=patients
    )


@pharmacy_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@role_required("admin", "pharmacist")
def edit(id):

    if request.method == "POST":

        update_medication(id, request.form)

        return redirect("/pharmacy/")

    medication = get_medication_by_id(id)

    patients = get_all_patients()

    return render_template(
        "pharmacy/edit.html",
        medication=medication,
        patients=patients
    )


@pharmacy_bp.route("/delete/<int:id>")
@role_required("admin")
def delete(id):

    delete_medication(id)

    return redirect("/pharmacy/")