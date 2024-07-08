from flask import Blueprint
from ..controllers import items_controllers

app = Blueprint('AddItem1', __name__)

app.route('/AddItem', methods=["POST"])(items_controllers.add_item)

app.route('/AddItem1',  methods=["POST", "GET"])(items_controllers.add_item1)