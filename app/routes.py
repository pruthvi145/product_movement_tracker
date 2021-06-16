from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import select, func

from app import app, db
from app.forms import ProductForm, LocationForm, ProductMovementForm
from app.models import Product, Location, ProductMovement, Report
from app.helpers import *

# -----------------        ROUTES - INDEX     -----------------------
@app.route("/")
@app.route("/index")
def index():
    """Route Controller - show the final generated report"""
    report = generate_report()
    return render_template("index.jinja", title="Home", report=report.get_all())


# -----------------       ROUTES - PRODUCTS     -----------------------
@app.route("/products", methods=["GET", "POST"])
def products():
    products = fetch_products()

    product_form = ProductForm()

    if product_form.validate_on_submit():
        product = Product(name=product_form.product_name.data)
        db.session.add(product)
        db.session.commit()

        flash(f"{product_form.product_name.data} added successfully!", "success")
        return redirect(url_for("products"))

    return render_template("products.jinja", products=products, form=product_form)


@app.route("/products/<id>", methods=["GET", "POST"])
def edit_product(id):
    product = Product.query.get(id)
    products = fetch_products()
    if not product:
        return redirect(url_for("/products"))

    product_form = ProductForm()

    if product_form.validate_on_submit():
        prev_product_name = product.name
        product.name = product_form.product_name.data
        db.session.commit()
        flash(
            f"{prev_product_name} has modified to {product.name} successfully!",
            "success",
        )
        return redirect(url_for("products"))

    return render_template(
        "products.jinja", products=products, form=product_form, current_product=product
    )


@app.route("/products/delete", methods=["POST"])
def delete_product():
    """Route Controller - Delete the product with product_id if exists"""

    product_id = request.form.get("product_id")
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash(f"{product.name} has deleted successfully!", "success")

    return redirect(url_for("products"))


# -----------------       ROUTES - LOCATIONS     -----------------------
@app.route("/locations", methods=["GET", "POST"])
def locations():
    locations = fetch_locations()

    location_form = LocationForm()
    if location_form.validate_on_submit():
        location = Location(name=location_form.location_name.data)
        db.session.add(location)
        db.session.commit()

        flash(f"{location_form.location_name.data} added successfully!", "success")
        return redirect(url_for("locations"))

    return render_template("locations.jinja", locations=locations, form=location_form)


@app.route("/locations/<id>", methods=["GET", "POST"])
def edit_location(id):
    current_location = Location.query.get(id)
    locations = fetch_locations()
    if not current_location:
        return redirect(url_for("locations"))

    location_form = LocationForm()

    if location_form.validate_on_submit():
        prev_location_name = current_location.name
        current_location.name = location_form.location_name.data
        db.session.commit()
        flash(
            f"{prev_location_name} has modified to {current_location.name} successfully!",
            "success",
        )
        return redirect(url_for("locations"))

    return render_template(
        "locations.jinja",
        locations=locations,
        form=location_form,
        current_location=current_location,
    )


@app.route("/locations/delete", methods=["POST"])
def delete_location():
    """Route Controller - Delete the location with location_id if exists"""

    location_id = request.form.get("location_id")
    location = Location.query.get(location_id)
    if location:
        db.session.delete(location)
        db.session.commit()
        flash(f"{location.name} has deleted successfully!", "success")

    return redirect(url_for("locations"))


# -----------------       ROUTES - PRODUCT MOVEMENT     -----------------------


@app.route("/product_movement", methods=["GET", "POST"])
def product_movement():
    form = ProductMovementForm()
    set_choices_for_product_movement_form(form)

    if form.validate_on_submit():
        product_id = form.product_id.data
        from_location_id = form.from_location_id.data
        to_location_id = form.to_location_id.data
        qty = form.qty.data

        # TODO: raise Validation error if from and to location both are not provided

        product_movement = ProductMovement(
            product_id=form.product_id.data,
            to_location_id=None if to_location_id == -1 else to_location_id,
            from_location_id=None if from_location_id == -1 else from_location_id,
            qty=qty,
        )
        db.session.add(product_movement)
        db.session.commit()

        flash(f"Product Movement made successfully!", "success")
        return redirect(url_for("product_movement"))

    product_movements = fetch_product_movements()
    return render_template(
        "product_movement.jinja",
        title="Product Mover",
        form=form,
        product_movements=product_movements,
    )


@app.route("/product_movement/delete", methods=["POST"])
def delete_product_movement():
    """Route Controller - Delete the product movement transaction with movement_id if exists"""

    product_movement_id = request.form.get("product_movement_id")
    product_movement = ProductMovement.query.get(product_movement_id)
    if product_movement:
        db.session.delete(product_movement)
        db.session.commit()
        flash(
            f"Transcation having {product_movement.id} as id has deleted successfully!",
            "success",
        )

    return redirect(url_for("product_movement"))
