from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf.csrf import CSRFProtect

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    bedrooms = IntegerField('Number of Bedrooms', validators=[InputRequired()])
    bathrooms = StringField('Number of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    property_type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo',validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg'], 'Images only!')] )
    