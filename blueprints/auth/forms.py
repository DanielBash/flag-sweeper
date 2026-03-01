""" - Registration form
 - Login form"""


# -- importing useful modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# -- registration form
class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=4, max=32, message='Username must be at least 4 characters, with the maximum of 32.')
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter your inbox email address in format: <name>@<host>.<domain>.')
        ]
    )
    password = PasswordField(
        'Come up with a password',
        validators=[
            DataRequired(),
            Length(min=8, message='Password must be at least 8 characters.')
        ]
    )
    confirm_password = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Log In')


class ProfileEditForm(FlaskForm):
    bio = TextAreaField(label='Bio', validators=[DataRequired(), Length(max=5000, message='Bio must be shorter then 5k symbols.')])
    status = StringField(label='Status', validators=[DataRequired(), Length(min=5, max=30, message='Status must be at least 5 charecters and no more then 30.')])
    submit = SubmitField('Apply')