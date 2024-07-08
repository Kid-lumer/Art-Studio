from flask import Blueprint
from ..controllers import user_controllers



app = Blueprint('signup', __name__)

app.route('/')(user_controllers.landing)


app.route('/signup',  methods=["POST", "GET"])(user_controllers.signup)

app.route('/login_buyer',  methods=["POST", "GET"])(user_controllers.buyer_login)

app.route('/profile', methods=["GET"])(user_controllers.getItems)

# app.route('/get_users', methods = {'GET'})(user_controllers.get_all_users)