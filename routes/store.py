from flask import Blueprint, render_template, request, redirect, url_for, session
from models import get_products, add_order

store_bp = Blueprint('store', __name__)

@store_bp.route('/store')
def store():
    products = get_products()
    return render_template('store.html', products=products)

@store_bp.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    products = get_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart = session.get('cart', {})
        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += 1
        else:
            cart[str(product_id)] = {'id': product_id, 'image': product['image'] ,'name': product['name'], 'price': product['price'], 'quantity': 1}
        session['cart'] = cart
    return redirect(url_for('store.store'))

@store_bp.route('/cart')
def cart():
    cart = session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total=total)

@store_bp.route('/checkout', methods=['POST'])
def checkout():
    cart = session.get('cart', {})
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    add_order(name, email, address, cart)
    session['cart'] = {}
    return redirect(url_for('store.store'))

@store_bp.route('/remove_all')
def remove_all():
    session['cart'] = {}
    return redirect(url_for('store.cart'))

@store_bp.route('/remove_one_id')
def remove_one_id(product_id):
    cart = session.get('cart', {})
    if product_id in cart:
        del cart[product_id]  
        request.session["cart"] = cart
    return redirect(url_for('store.cart'))