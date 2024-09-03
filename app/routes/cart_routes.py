from flask import Blueprint
from ..controllers import cart_controllers

app = Blueprint('cart_bp', __name__)



app.route('/ViewCart', methods=['POST', 'GET'])(cart_controllers.cart)
app.route('/AddToCart', methods=['POST', 'GET'])(cart_controllers.add_to_cart)
app.route('/cart/remove', methods=['POST'])(cart_controllers.remove_from_cart)
app.route('/update_quantity', methods=['POST'])(cart_controllers.update_quantity)
app.route('/checkout',  methods=['POST'])(cart_controllers.checkout)
app.route('/process_payment', methods=['POST'])(cart_controllers.process_payment)
app.route('/thankyou')(cart_controllers.thank_you)
app.route('/payment_success')(cart_controllers.payment_success)