from flask import request, jsonify, render_template, session, url_for, redirect
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

       
        items = Products.find_items()
        cart_count = len(session.get('cart', []))
        return render_template("profile.html", item=items, cart_count=cart_count)
    return "Success"

def getItems():
    items = Products.find_items()
    cart_count = len(session.get('cart', []))
    return render_template("profile.html", item=items, cart_count=cart_count)


def getCatalog():
    items = Products.find_items()
    cart_count = len(session.get('cart', []))
    return render_template("catalog.html", item=items, cart_count=cart_count)



def delete_product():
     if request.method == 'POST':
        product_id = request.form['delete_id']
        Products.delete_item(product_id)
        
    
     cart_count = len(session.get('cart', []))
     return redirect(url_for('items_bp.getItems'))

def view():
    if request.method == 'POST':
        id = request.form['id']
        Name = request.form['Name']
        Amount = request.form['Amount']
        Description = request.form['Description']
        image = request.form['image']
        cart_count = len(session.get('cart', []))
        return render_template('ViewItem.html', id=id, Name=Name, Description=Description, Amount=Amount, image=image, cart_count=cart_count)

def edit_item():
    if request.method == 'POST':
        update_id = request.form['update_id']
        email = request.form['email']
        item_id = ObjectId(update_id)
        cart_count = len(session.get('cart', []))
        return render_template("edit.html", item_id=item_id, email=email, cart_count=cart_count)
    

def edit_item2():
    if request.method == 'POST':
        update_id = request.form['update_id']
        email = request.form['email']
        name = request.form['Name']
        Amount = request.form['Amount']
        description = request.form['Description']
        image = request.form['image']
        item_id = ObjectId(update_id)
        Products.edit_item({'_id': item_id}, {'$set': {'Name': name, 'email': email, 'Description': description, 'Amount': Amount, 'image': image}})
        items = Products.find_items({'email': email})
        cart_count = len(session.get('cart', []))
        return redirect(url_for('items_bp.edit_item2'), item=items, cart_count=cart_count)