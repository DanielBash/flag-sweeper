""" - Before request handlers"""

from flask import g, session, current_app
from ..models import User


@current_app.before_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)