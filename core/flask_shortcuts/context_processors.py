"""- All context processors for flask"""

# -- importing modules
from flask import current_app, g


@current_app.context_processor
def inject_user():
    return dict(user=g.user)