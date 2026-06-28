from flask import Blueprint, jsonify, request

from models.appointment import (
    get_all_appointments,
    get_appointment_by_id,
    create_appointment,
    update_appointment,
    delete_appointment
)

appointments_api_bp = Blueprint(
    "appointments_api",
    __name__,
    url_prefix="/api/appointments"
)


@appointments_api_bp.route("/", methods=["GET"])
def api_list_appointments():

    return jsonify(
        get_all_appointments()
    )


@appointments_api_bp.route("/<int:id>", methods=["GET"])
def api_get_appointment(id):

    appointment = get_appointment_by_id(id)

    if not appointment:

        return jsonify({
            "error": "Appointment not found"
        }), 404

    return jsonify(appointment)


@appointments_api_bp.route("/", methods=["POST"])
def api_create_appointment():

    data = request.get_json()

    create_appointment(data)

    return jsonify({
        "message": "Appointment created successfully"
    }), 201


@appointments_api_bp.route("/<int:id>", methods=["PUT"])
def api_update_appointment(id):

    data = request.get_json()

    update_appointment(id, data)

    return jsonify({
        "message": "Appointment updated successfully"
    })


@appointments_api_bp.route("/<int:id>", methods=["DELETE"])
def api_delete_appointment(id):

    delete_appointment(id)

    return jsonify({
        "message": "Appointment deleted successfully"
    })