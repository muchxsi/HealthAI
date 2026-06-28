from flask import Blueprint, jsonify, request

from models.pharmacy import (
    get_all_medications,
    get_medication_by_id,
    create_medication,
    update_medication,
    delete_medication
)

pharmacy_api_bp = Blueprint(
    "pharmacy_api",
    __name__,
    url_prefix="/api/pharmacy"
)


@pharmacy_api_bp.route("/", methods=["GET"])
def api_list_medications():

    return jsonify(get_all_medications())


@pharmacy_api_bp.route("/<int:id>", methods=["GET"])
def api_get_medication(id):

    medication = get_medication_by_id(id)

    if not medication:

        return jsonify({
            "error": "Medication not found"
        }), 404

    return jsonify(medication)


@pharmacy_api_bp.route("/", methods=["POST"])
def api_create_medication():

    data = request.get_json()

    create_medication(data)

    return jsonify({
        "message": "Medication created successfully"
    }), 201


@pharmacy_api_bp.route("/<int:id>", methods=["PUT"])
def api_update_medication(id):

    data = request.get_json()

    update_medication(id, data)

    return jsonify({
        "message": "Medication updated successfully"
    })


@pharmacy_api_bp.route("/<int:id>", methods=["DELETE"])
def api_delete_medication(id):

    delete_medication(id)

    return jsonify({
        "message": "Medication deleted successfully"
    })