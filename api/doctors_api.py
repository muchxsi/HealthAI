from flask import Blueprint, jsonify, request

from models.doctor import (
    get_all_doctors,
    get_doctor_by_id,
    create_doctor,
    update_doctor,
    delete_doctor
)

doctors_api_bp = Blueprint(
    "doctors_api",
    __name__,
    url_prefix="/api/doctors"
)


@doctors_api_bp.route("/", methods=["GET"])
def api_list_doctors():

    return jsonify(get_all_doctors())


@doctors_api_bp.route("/<int:id>", methods=["GET"])
def api_get_doctor(id):

    doctor = get_doctor_by_id(id)

    if not doctor:

        return jsonify({
            "error": "Doctor not found"
        }), 404

    return jsonify(doctor)


@doctors_api_bp.route("/", methods=["POST"])
def api_create_doctor():

    data = request.get_json()

    create_doctor(data)

    return jsonify({
        "message": "Doctor created successfully"
    }), 201


@doctors_api_bp.route("/<int:id>", methods=["PUT"])
def api_update_doctor(id):

    data = request.get_json()

    update_doctor(id, data)

    return jsonify({
        "message": "Doctor updated successfully"
    })


@doctors_api_bp.route("/<int:id>", methods=["DELETE"])
def api_delete_doctor(id):

    delete_doctor(id)

    return jsonify({
        "message": "Doctor deleted successfully"
    })