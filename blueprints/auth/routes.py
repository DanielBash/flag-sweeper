""" - Main page bluprint
 -- Docs can be added soon"""

# -- importing modules
import datetime
from flask import current_app, flash, redirect, url_for, session
from flask import Blueprint, render_template
from core.core import register_user, check_credentials
from core.models import User
from .forms import RegistrationForm, LoginForm


bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = register_user(username=form.data['username'],
                             password=form.data['password'],
                             email=form.data['email'])
        if user is None:
            flash('This username already exists, sorry.', 'Warning')
            return render_template('register.html', form=form, title='FS: Registration')
        else:
            session['user_id'] = user.id
            flash('Registration successful!', 'Success')
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form, title='FS: Registration')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if check_credentials(form.data['username'], form.data['password']):
            flash('Login successful!', 'Success')
            session['user_id'] = User.query.filter_by(username=form.data['username']).first().id
            return redirect(url_for('main.index'))
        else:
            flash('Incorrect credentials!', 'Warning')
            return redirect(url_for('auth.login'))
    return render_template('login.html', form=form, title='FS: Login')
