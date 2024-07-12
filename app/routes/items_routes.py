from flask import Blueprint
from ..controllers import items_controllers

app = Blueprint('AddItem1', __name__)

app.route('/AddItem', methods=["POST", "GET"])(items_controllers.add_item)

app.route('/AddItem1',  methods=["POST", "GET"])(items_controllers.add_item1)

app.route('/getCatalog', methods = ["POST", "GET"])(items_controllers.getCatalog)

app.route('/delete_item', methods=["POST"])(items_controllers.delete_product)