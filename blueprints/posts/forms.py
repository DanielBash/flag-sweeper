""" - Publish post form"""


# -- importing useful modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# -- registration form
class PostForm(FlaskForm):
    subject = StringField(
        'Subject',
        validators=[
            DataRequired(),
            Length(min=5, max=32, message='Subject must be from 5 to 32 symbols')
        ]
    )
    
    content = TextAreaField(
        'Content',
        validators=[
            DataRequired(),
            Length(min=5, max=5000, message='Content must be from 5 to 5k symbols')
        ]
    )

    submit = SubmitField('Publish')