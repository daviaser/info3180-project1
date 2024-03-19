from . import db
from werkzeug.security import generate_password_hash


class Property(db.Model):
    __tablename__ = 'Property Listings'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.String(100))
    location = db.Column(db.String(100))
    price = db.Column(db.String(100))
    property_type = db.Column(db.String(80))
    description = db.Column(db.Text)
    photo = db.Column(db.String(255))
    

    def __init__(self, title, bedrooms, bathrooms, location, price, property_type, description, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.description = description
        self.photo = photo
    
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.id)