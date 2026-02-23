"""- Core functions, and overall app logic"""

# -- importing modules
from .flask_shortcuts import initialize_app


def create_app(name):
    return initialize_app.create_app(name)
