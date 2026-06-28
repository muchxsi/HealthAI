from flask import Blueprint, jsonify, request

from models.patient import (
    get_all_patients,
    get_patient_by_id,
    create_patient,
    update_patient,
    delete_patient
)

patients_api_bp = Blueprint(
    "patients_api",
    __name__,
    url_prefix="/api/patients"
)


@patients_api_bp.route("/", methods=["GET"])
def api_list_patients():

    return jsonify(
        get_all_patients()
    )


@patients_api_bp.route("/<int:id>", methods=["GET"])
def api_get_patient(id):

    patient = get_patient_by_id(id)

    if not patient:

        return jsonify(
            {
                "error": "Patient not found"
            }
        ), 404

    return jsonify(patient)


@patients_api_bp.route("/", methods=["POST"])
def api_create_patient():

    data = request.get_json()

    create_patient(data)

    return jsonify(
        {
            "message": "Patient created successfully"
        }
    ), 201


@patients_api_bp.route("/<int:id>", methods=["PUT"])
def api_update_patient(id):

    data = request.get_json()

    update_patient(id, data)

    return jsonify(
        {
            "message": "Patient updated successfully"
        }
    )


@patients_api_bp.route("/<int:id>", methods=["DELETE"])
def api_delete_patient(id):

    delete_patient(id)

    return jsonify(
        {
            "message": "Patient deleted successfully"
        }
    )