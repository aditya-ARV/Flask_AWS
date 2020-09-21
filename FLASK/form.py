from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class AddProduct(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=4,max=20)])
    family = StringField('Family',validators=[DataRequired(),Length(min=2,max=20)])
    flash = PasswordField('Flash',validators=[DataRequired()])
    flash_confirm = PasswordField('Flash',validators=[DataRequired(),EqualTo('flash')])
    submit = SubmitField('Add')

class ViewProduct(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=4,max=20)])
    submit = SubmitField('View')

    
