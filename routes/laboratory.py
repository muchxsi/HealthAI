from flask import Blueprint, render_template, request, redirect

from utils.roles import role_required

from models.laboratory import (
    get_all_tests,
    create_test,
    get_test_by_id,
    update_test,
    delete_test,
    search_tests
)

from models.patient import get_all_patients


laboratory_bp = Blueprint(
    "laboratory",
    __name__,
    url_prefix="/laboratory"
)


@laboratory_bp.route("/")
@role_required("admin", "lab_technician")
def list_tests():

    keyword = request.args.get("search")

    if keyword:

        tests = search_tests(keyword)

    else:

        tests = get_all_tests()

    return render_template(
        "laboratory/list.html",
        tests=tests
    )


@laboratory_bp.route("/create", methods=["GET", "POST"])
@role_required("admin", "lab_technician")
def create():

    if request.method == "POST":

        create_test(request.form)

        return redirect("/laboratory/")

    patients = get_all_patients()

    return render_template(
        "laboratory/create.html",
        patients=patients
    )


@laboratory_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@role_required("admin", "lab_technician")
def edit(id):

    if request.method == "POST":

        update_test(id, request.form)

        return redirect("/laboratory/")

    test = get_test_by_id(id)

    patients = get_all_patients()

    return render_template(
        "laboratory/edit.html",
        test=test,
        patients=patients
    )


@laboratory_bp.route("/delete/<int:id>")
@role_required("admin")
def delete(id):

    delete_test(id)

    return redirect("/laboratory/")