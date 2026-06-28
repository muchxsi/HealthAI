from flask import Blueprint, render_template, request, redirect

from utils.roles import role_required

from models.billing import (
    get_all_bills,
    create_bill,
    get_bill_by_id,
    update_bill,
    delete_bill,
    search_bills
)

from models.patient import get_all_patients


billing_bp = Blueprint(
    "billing",
    __name__,
    url_prefix="/billing"
)


@billing_bp.route("/")
@role_required("admin", "receptionist")
def list_bills():

    keyword = request.args.get("search")

    if keyword:

        bills = search_bills(keyword)

    else:

        bills = get_all_bills()

    return render_template(
        "billing/list.html",
        bills=bills
    )


@billing_bp.route("/create", methods=["GET", "POST"])
@role_required("admin", "receptionist")
def create():

    if request.method == "POST":

        create_bill(request.form)

        return redirect("/billing/")

    patients = get_all_patients()

    return render_template(
        "billing/create.html",
        patients=patients
    )


@billing_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@role_required("admin", "receptionist")
def edit(id):

    if request.method == "POST":

        update_bill(id, request.form)

        return redirect("/billing/")

    bill = get_bill_by_id(id)

    patients = get_all_patients()

    return render_template(
        "billing/edit.html",
        bill=bill,
        patients=patients
    )


@billing_bp.route("/delete/<int:id>")
@role_required("admin")
def delete(id):

    delete_bill(id)

    return redirect("/billing/")