from flask import Blueprint, jsonify, request

from models.laboratory import (
    get_all_tests,
    get_test_by_id,
    create_test,
    update_test,
    delete_test
)

laboratory_api_bp = Blueprint(
    "laboratory_api",
    __name__,
    url_prefix="/api/laboratory"
)


@laboratory_api_bp.route("/", methods=["GET"])
def api_list_tests():

    return jsonify(get_all_tests())


@laboratory_api_bp.route("/<int:id>", methods=["GET"])
def api_get_test(id):

    test = get_test_by_id(id)

    if not test:

        return jsonify({
            "error": "Test not found"
        }), 404

    return jsonify(test)


@laboratory_api_bp.route("/", methods=["POST"])
def api_create_test():

    create_test(request.get_json())

    return jsonify({
        "message": "Laboratory test created successfully"
    }), 201


@laboratory_api_bp.route("/<int:id>", methods=["PUT"])
def api_update_test(id):

    update_test(id, request.get_json())

    return jsonify({
        "message": "Laboratory test updated successfully"
    })


@laboratory_api_bp.route("/<int:id>", methods=["DELETE"])
def api_delete_test(id):

    delete_test(id)

    return jsonify({
        "message": "Laboratory test deleted successfully"
    })