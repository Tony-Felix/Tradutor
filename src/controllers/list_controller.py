from flask import Blueprint, jsonify

from models.history_model import HistoryModel


list_controller = Blueprint("list_controller", __name__)


@list_controller.route("/", methods=["GET"])
def history_get():
    result_list_json = HistoryModel.list_as_json()
    return jsonify(result_list_json), 200
