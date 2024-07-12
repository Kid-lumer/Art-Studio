from flask import request, jsonify, render_template, session
from ..models.items import Products
from bson.objectid import ObjectId

def add_item():
    if request.method == 'POST':
        return render_template("/AddItem.html")
    return render_template("AddItem.html")


def add_item1():
    if request.method == 'POST':
        Name = request.form['Name']
        email = request.form['email']
        Amount = request.form['Amount']
        Description = request.form['Description']
        image = request.form['image']

        item = {'Name': Name, 'email': email, 'Amount': Amount, 'Description': Description, 'image': image}
        Products.create_item(item)

       
        items = Products.find_item()
        cart_count = len(session.get('cart', []))
        return render_template("profile.html", item=items, cart_count=cart_count)
    return "Success"

def getItems():
    items = ()
    cart_count = len(session.get('cart', []))
    return render_template("profile.html", item=items, cart_count=cart_count)


def getCatalog():
    items = list(Products.find_item())
    cart_count = len(session.get('cart', []))
    return render_template("catalog.html", item=items, cart_count=cart_count)


def delete_product():
    if request.method == 'POST':
        delete_id = request.form['delete_id']
        Products.delete_product.delete_one({"_id": ObjectId(delete_id)})
    items = list(Products.delete_product.find())
    cart_count = len(session.get('cart', []))
    return render_template("profile.html", item=items, cart_count=cart_count)