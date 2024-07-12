from flask import request, jsonify, render_template, session, redirect, url_for, flash
from ..models.user import New
from ..models.items import Products



def landing():
    full_name = session.get('full_name', 'Guest')
    cart_count = len(session.get('cart', []))
    return render_template("index.html", cart_count=cart_count, full_name=full_name )


#Signup
def signup():
    if request.method == "POST":
        full_name = request.form["name"]
        email = request.form["email"]
        cell_no = request.form["CellNo."]
        password = request.form["password"]
        role = request.form['role']
        signup_details = {"full_name": full_name, "email": email, "Cell_No": cell_no, "password": password, 'role': role}

        # check if user exists using email
        existing_user = New.find_by_email(email)
        if existing_user:
            flash("Email already exists. Please use a different email.")
            return render_template('register.html', success=False)

        # Create a new user
        New.create_user(signup_details)
        print(signup_details)

       
        if signup_details:
            return render_template('register.html', success=True)
        else:
            return render_template('register.html', success=False)
    return render_template('register.html'), 200
#Login
def buyer_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['signin_password']
        role = request.form['role']
        
        user = {'email': email, 'password': password, 'role': role}
        New.login(user)
   
   
    return render_template("profile.html")


def getItems():
    items = Products.create_item()
    cart_count = len(session.get('cart', []))
    return render_template("profile.html", item=items, cart_count=cart_count)

