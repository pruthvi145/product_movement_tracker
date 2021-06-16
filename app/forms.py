from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange, ValidationError

from app.validators import SelectionRequired


class ProductForm(FlaskForm):
    product_id = StringField("Product ID")
    product_name = StringField("Product Name", validators=[DataRequired()])
    submit = SubmitField("Add Product")


class LocationForm(FlaskForm):
    location_id = StringField("Location ID")
    location_name = StringField("Location Name", validators=[DataRequired()])
    submit = SubmitField("Add Location")


class ProductMovementForm(FlaskForm):
    product_id = SelectField(
        "Products",
        coerce=int,
        validators=[SelectionRequired(message="Product is required!")],
    )
    from_location_id = SelectField("From Location", coerce=int, validators=[])
    to_location_id = SelectField("To Location", coerce=int, validators=[])
    qty = IntegerField(
        "Product Quantity",
        validators=[
            DataRequired(message="Product quantity must be 1 or more!"),
            NumberRange(min=1, message="Product quantity must be 1 or more!"),
        ],
    )
