from flask import Blueprint, request, jsonify
from my_project.auth.service.general_service import GeneralService

class GeneralController:
    def __init__(self):
        self.service = GeneralService()

    def get_items(self):
        items = self.service.get_all_items()
        return jsonify(items)

    def create_item(self):
        data = request.get_json()
        item = self.service.create_item(data)
        return jsonify(item), 201

# Blueprint setup
general_controller_bp = Blueprint('general_controller', __name__)

@general_controller_bp.route('/items', methods=['GET'])
def get_items():
    controller = GeneralController()
    return controller.get_items()

@general_controller_bp.route('/items', methods=['POST'])
def create_item():
    controller = GeneralController()
    return controller.create_item()