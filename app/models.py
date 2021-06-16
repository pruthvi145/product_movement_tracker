from app import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Product({self.id}, {self.name})"


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Location({self.id}, {self.name})"


class ProductMovement(db.Model):
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    from_location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    to_location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    qty = db.Column(db.Integer)
    timestemp = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations
    product = db.relationship("Product", foreign_keys=[product_id])
    to_location = db.relationship("Location", foreign_keys=[to_location_id])
    from_location = db.relationship("Location", foreign_keys=[from_location_id])

    def __repr__(self):
        return f"ProductMovement(id={self.id}, product_id={self.product_id}, product={self.product}, qty={self.qty}, from_location_id={self.from_location_id}, to_location_id={self.to_location_id}, timestemp={self.timestemp}, to_location={self.to_location}, from_location={self.from_location} )"


# ---------------
# DUMB Models
# ---------------
# I am refering DUMB models which are not connecting to the databases.
# The main purpose of these types of models to use internally.


class Report:
    """Report Model is used for storing the generated report."""

    def __init__(self):
        self.report = []
        self.count = 0

    def add(self, product, location, qty):
        self.count += 1
        self.report.append(_ReportRow(self.count, product, location, qty))

    def get(self, id):
        # TODO: handle value error
        return list(filter(lambda row: row.id == id, self.report))[0]

    def get_all(self):
        return self.report

    def __repr__(self):
        return f"Report(report={self.report})"


class _ReportRow:
    def __init__(self, id, product, location, qty):
        self.id = id
        self.product = product
        self.location = location
        self.qty = qty

    def __repr__(self):
        return f"ReportRow(id={self.id}, product={self.product}, qty={self.qty}, location={self.location} )"
