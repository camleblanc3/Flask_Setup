from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PokeForm(FlaskForm):
    pokename = StringField('Poke Name', validators =[DataRequired()])
    submit = SubmitField()