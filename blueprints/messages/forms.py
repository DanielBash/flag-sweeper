""" - Send message form"""


# -- importing useful modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# -- registration form
class MessageForm(FlaskForm):
    reciever_username = StringField(
        'Reciever',
        validators=[
            DataRequired(),
            Length(min=4, max=32, message='Username must be at least 4 characters, with the maximum of 32.')
        ]
    )
    
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

    submit = SubmitField('Send')