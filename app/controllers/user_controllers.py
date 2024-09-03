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

        if New.find_user_by_email(email):
            print("Already exist")
            flash('Email or username already exist. Please try again with different credentials.', 'error')
        else:
            print("Succesful")

        if not New.create_user(signup_details):
            flash('Email or username already exist. Please try again with different credentials.', 'error')
            #Redirect to register page
            return render_template('register.html',  success=True)
        #Redirect to register page without error message 
        return render_template('register.html',  success=True)

        
    return render_template('register.html'), 200

#Login
def buyer_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['signin_password']
        role = request.form['role']
        
        known_user = New.find_user_by_email_and_password(email, password)

        if known_user:
            session['user_id'] = str(known_user['_id'])
            session['role'] = role
            if role == 'artist':
                items = Products.find_items()
                return render_template("profile.html", items = items)
            else:
                return render_template("catalog.html",)
           
    return render_template("register.html")

