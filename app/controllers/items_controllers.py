from flask import request, jsonify, render_template, session
from ..models.items import Products
from .. import mongo

def add_item():
    if request.method == 'POST':
        return render_template("AddItem.html")
    return render_template("AddItem.html")


def add_item1():
    if request.method == 'POST':
        Name = request.form['Name']
        email = request.form['email']
        Amount = request.form['Amount']
        Description = request.form['Description']
        image = request.form['image']

        item = {'Name': Name, 'email': email, 'Amount': Amount, 'Description': Description, 'image': image}
        Products.creat_item(item)

        mongo.db.Items.insert_one(item)
        items = mongo.db.Items.find()
        cart_count = len(session.get('cart', []))
        return render_template("profile.html", item=items, cart_count=cart_count)
    return "Success"