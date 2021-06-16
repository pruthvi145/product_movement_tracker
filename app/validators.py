from wtforms.validators import DataRequired, NumberRange, ValidationError


class SelectionRequired:
    """Raise ValidationError if no option selected for the select input type."""

    def __init__(self, message=None):
        if not message:
            message = "Please select an item!"
        self.message = message

    def __call__(self, form, field):
        if field.data == -1:
            raise ValidationError(self.message)
