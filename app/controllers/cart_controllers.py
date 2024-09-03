from flask import request, jsonify, render_template, session, url_for, redirect
from ..models.cart import Cart
from bson.objectid import ObjectId

def cart():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['Amount']) * item['quantity'] for item in cart_items)
    print("total price for view", total_price)
    cart_count = len(session.get('cart', []))
    session['total_price'] = total_price
    return render_template('ViewCart.html', cart_items=cart_items, total_price=total_price, cart_count=cart_count)

def add_to_cart():
    id = request.form.get('id')
    Name = request.form.get('Name')
    Amount = request.form.get('Amount')
    image = request.form['image']

    # Create item with quantity set to 1
    new_item = {'id': id, 'Name': Name, 'Amount': Amount, 'image': image, 'quantity': 1}

    cart_items = session.get('cart', [])
    item_exists = False

    # Check if item already exists in cart
    for item in cart_items:
        if item['id'] == new_item['id']:
            item['quantity'] += 1
            item['total_amount'] = sum(float(item['Amount']) * item['quantity'] for item in cart_items if item['id'] == id)

            item_exists = True
            break

    total_price = sum(float(item['Amount']) * item['quantity'] for item in cart_items)
    session['total_price'] = total_price
    # If item does not exist, append it to the cart
    if not item_exists:
        cart_items.append(new_item)

    session['cart'] = cart_items

    return redirect(url_for('cart_bp.cart'))


def remove_from_cart():
    selected_items = request.form.get('selected_items')
    cart_items = session.get('cart', [])
    cart_items = [item for item in cart_items if item['id'] != selected_items]
    session['cart'] = cart_items
    
    return redirect(url_for('cart_bp.cart'))

def update_quantity():
    item_id = request.form.get('id')
    new_quantity = int(request.form.get('quantity'))
    cart_items = session.get('cart', [])

    # Find the item and update its quantity
    for item in cart_items:
        if item['id'] == item_id:
            item['quantity'] = new_quantity
            item['total_amount'] = sum(float(item['Amount']) * item['quantity'] for item in cart_items if item['id'] == item_id)

            break

    session['cart'] = cart_items

    # Recalculate the total price of the updated item
    item_price = sum(float(item['Amount']) * item['quantity'] for item in cart_items if item['id'] == item_id)

    # Recalculate total price
    total_price = sum(float(item['Amount']) * item['quantity'] for item in cart_items)
    session['total_price'] = total_price
    session['item_price'] = item_price
    print("item price", cart_items)
    print("total price for update", total_price)
    # Return the updated prices as JSON
    return jsonify({'success': True, 'item_price': item_price, 'total': total_price})

def checkout():
    cart_items = session.get('cart', [])
    amount = session.get('total_amount')
    total_price = session.get('total_price')

    print("t2", amount)
    
    item_price = session.get('item_price')
    # return redirect(url_for('cart_bp.process_payment', cart_items=cart_items, total_price=total_price))
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)


def process_payment():
    # Here you would add your payment processing logic
    card_number = request.form['cardNumber']
    expiry_date = request.form['expiryDate']
    cvv = request.form['cvv']
    card_holder_name = request.form['cardHolderName']
    
    # Dummy processing logic (to be replaced with actual payment gateway integration)
    if card_number and expiry_date and cvv and card_holder_name:
        # Clear the cart after successful payment
        session['cart'] = []
        return redirect(url_for('thank_you'))
    else:
        return redirect(url_for('payment_failure'))
    

def thank_you():
    return render_template("thankyou.html")

def payment_success():
    return "Payment was successful! Thank you for your purchase."