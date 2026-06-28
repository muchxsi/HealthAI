from flask import Blueprint, jsonify, request

from models.medical_record import (
    get_all_records,
    get_record_by_id,
    create_record,
    update_record,
    delete_record
)

medical_records_api_bp = Blueprint(
    "medical_records_api",
    __name__,
    url_prefix="/api/medical-records"
)


@medical_records_api_bp.route("/", methods=["GET"])
def api_list_records():

    return jsonify(
        get_all_records()
    )


@medical_records_api_bp.route("/<int:id>", methods=["GET"])
def api_get_record(id):

    record = get_record_by_id(id)

    if not record:

        return jsonify({
            "error": "Medical record not found"
        }), 404

    return jsonify(record)


@medical_records_api_bp.route("/", methods=["POST"])
def api_create_record():

    data = request.get_json()

    create_record(data)

    return jsonify({
        "message": "Medical record created successfully"
    }), 201


@medical_records_api_bp.route("/<int:id>", methods=["PUT"])
def api_update_record(id):

    data = request.get_json()

    update_record(id, data)

    return jsonify({
        "message": "Medical record updated successfully"
    })


@medical_records_api_bp.route("/<int:id>", methods=["DELETE"])
def api_delete_record(id):

    delete_record(id)

    return jsonify({
        "message": "Medical record deleted successfully"
    })