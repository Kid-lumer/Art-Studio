from flask import Blueprint
from ..controllers import items_controllers

app = Blueprint('items_bp', __name__)

app.route('/AddItem', methods=["POST", "GET"])(items_controllers.add_item)

app.route('/AddItem1',  methods=["POST", "GET"])(items_controllers.add_item1)

app.route('/getCatalog', methods = ["POST", "GET"])(items_controllers.getCatalog)

app.route('/delete_item', methods=["POST"])(items_controllers.delete_product)

app.route('/admin_products', methods = ["POST", "GET"])(items_controllers.getItems)

app.route('/viewproduct', methods=['GET', 'POST'])(items_controllers.view)

app.route('/Edit', methods=['POST'])(items_controllers.edit_item)

app.route('/Edit2', methods=['POST'])(items_controllers.edit_item2)