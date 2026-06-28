from flask import Blueprint, jsonify, request

from models.billing import (
    get_all_bills,
    get_bill_by_id,
    create_bill,
    update_bill,
    delete_bill
)

billing_api_bp = Blueprint(
    "billing_api",
    __name__,
    url_prefix="/api/billing"
)


@billing_api_bp.route("/", methods=["GET"])
def api_list_bills():

    return jsonify(
        get_all_bills()
    )


@billing_api_bp.route("/<int:id>", methods=["GET"])
def api_get_bill(id):

    bill = get_bill_by_id(id)

    if not bill:

        return jsonify({
            "error": "Bill not found"
        }), 404

    return jsonify(bill)


@billing_api_bp.route("/", methods=["POST"])
def api_create_bill():

    data = request.get_json()

    create_bill(data)

    return jsonify({
        "message": "Bill created successfully"
    }), 201


@billing_api_bp.route("/<int:id>", methods=["PUT"])
def api_update_bill(id):

    data = request.get_json()

    update_bill(id, data)

    return jsonify({
        "message": "Bill updated successfully"
    })


@billing_api_bp.route("/<int:id>", methods=["DELETE"])
def api_delete_bill(id):

    delete_bill(id)

    return jsonify({
        "message": "Bill deleted successfully"
    })