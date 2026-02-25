""" - Main page bluprint
 -- Docs can be added soon"""

# -- importing modules
import datetime
from flask import current_app, flash, redirect, url_for
from flask import Blueprint, render_template
from .forms import RegistrationForm, LoginForm


bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Registration successful!', 'success')
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form, title='FS: Registration')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful!', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form, title='FS: Login')
