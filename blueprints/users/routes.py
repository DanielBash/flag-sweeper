""" - User accounts views"""


# -- importing modules
import datetime
from flask import current_app, flash
from flask import Blueprint, render_template
from core.models import User

bp = Blueprint('users', __name__)


@bp.route('/<string:username>', methods=['GET'])
def user(username):
    target_user = User.query.filter_by(username=username).first_or_404()
    
    return render_template('user.html', title=f'FS: {username}', target_user=target_user)