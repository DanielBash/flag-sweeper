""" - Machine creation form"""


# -- importing useful modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import settings


# -- machine creation form
class MachineForm(FlaskForm):
    distro = SelectField('Distro', choices = settings.ALLOWED_IMAGES, validators = [DataRequired()])

    submit = SubmitField('Create')