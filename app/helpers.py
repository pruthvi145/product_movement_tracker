from app.forms import ProductMovementForm

from app.models import Product, Location, ProductMovement, Report


def fetch_products():
    return Product.query.all()


def fetch_locations():
    return Location.query.all()


def fetch_product_movements():
    return ProductMovement.query.all()


def set_choices_for_product_movement_form(form: ProductMovementForm):
    default_product_choice = [(-1, "Select Product")]
    default_location_choice = [(-1, "Select Location")]

    products = [(product.id, product.name) for product in fetch_products()]
    locations = [(location.id, location.name) for location in fetch_locations()]

    form.product_id.choices = default_product_choice + products
    form.to_location_id.choices = form.from_location_id.choices = (
        default_location_choice + locations
    )


def generate_report():
    all_movements = fetch_product_movements()
    all_products = fetch_products()
    all_locations = fetch_locations()
    report = Report()

    # from_movements = (
    #     db.session.query(
    #         ProductMovement.product,
    #         ProductMovement.from_location,
    #         func.sum(ProductMovement.qty),
    #     )
    #     .filter(ProductMovement.from_location_id != None)
    #     .group_by(ProductMovement.product_id, ProductMovement.from_location_id)
    #     .all()
    # )
    # to_movements = (
    #     db.session.query(
    #         ProductMovement.product_id,
    #         ProductMovement.to_location_id,
    #         func.sum(ProductMovement.qty),
    #     )
    #     .filter(ProductMovement.to_location_id != None)
    #     .group_by(ProductMovement.product_id, ProductMovement.to_location_id)
    #     .all()
    # )

    for product in all_products:
        for location in all_locations:
            from_qty = sum(
                [
                    row.qty
                    for row in all_movements
                    if row.product_id == product.id
                    and row.from_location_id == location.id
                ]
            )
            to_qty = sum(
                [
                    row.qty
                    for row in all_movements
                    if row.product_id == product.id
                    and row.to_location_id == location.id
                ]
            )

            if not from_qty and not to_qty:
                continue
            balanced_qty = to_qty - from_qty
            report.add(product, location, balanced_qty)

    return report
