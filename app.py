"""Shopping cart application."""

from flask import Flask, request, session, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from products import Product

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

cart = []

@app.route("/")
def homepage():
    """Homepage: show list of products with link to product page."""
    all_products = Product.get_all()
    
    return render_template("homepage.html", allproducts=all_products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    """Show detail of product, along with add-to-cart form."""
    product = Product.get_by_id(product_id)

    return render_template("product.html", product=product)

@app.route("/cart")
def show_cart():
    """Show shopping cart."""

    return render_template("cart.html")


@app.route("/add-to-cart", methods=["POST"])
def add_cart():
    # get the id from the form
    # find the product by the id we got from the form
    product_id = int(request.form.get("product-id"))
    product = Product.get_by_id(product_id)
    cart.append(product)
    # redirect to f"/products/{id}"
    return redirect(f'/products/{product_id}')
# missing routes:
#   /add-to-cart
#   /clear-cart   [in further study]
