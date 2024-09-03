from flask import Blueprint
from ..controllers import user_controllers



app = Blueprint('signup', __name__)

app.route('/')(user_controllers.landing)

app.route('/signup',  methods=["POST", "GET"])(user_controllers.signup)

app.route('/login_buyer',  methods=["POST", "GET"])(user_controllers.buyer_login)

