from flask import request, jsonify, render_template, session
from ..models.user import New
from .. import mongo


def landing():
    full_name = session.get('full_name', 'Guest')
    cart_count = len(session.get('cart', []))
    return render_template("index.html", cart_count=cart_count, full_name=full_name )



def signup():
    if request.method == "POST":
        full_name = request.form["name"]
        email = request.form["email"]
        cell_no = request.form["CellNo."]
        password = request.form["password"]
        role = request.form['role']

        print("fn", full_name)
        print(email)
        print(cell_no)
        print(password)
        print(role)

        signup_details = {"full_name": full_name, "email": email, "Cell_No": cell_no, "password": password, 'role': role}
        New.create_user(signup_details)
        print(signup_details)

       
        if signup_details:
            return render_template('register.html', success=True)
        else:
            return render_template('register.html', success=False)
    return render_template('register.html'), 200

def buyer_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['signin_password']
        role = request.form['role']
        
        user = {'email': email, 'password': password, 'role': role}
        New.login(user)


        if user:
            session['user_id'] = str(user['_id'])
            session['role'] = role
            cart_count = len(session.get('cart', []))
            if role == 'artist':
                items = mongo.db.Items.find({'email': email})
                return render_template("profile.html", item=items, cart_count=cart_count)
            else:
                items = mongo.db.Items.find()
                return render_template("catalog.html", item=items, cart_count=cart_count)
    return render_template("login.html")


def getItems():
    items = mongo.db.Items.find()
    cart_count = len(session.get('cart', []))
    return render_template("profile.html", item=items, cart_count=cart_count)