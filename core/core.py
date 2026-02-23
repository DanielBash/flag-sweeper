"""- Core functions, and overall app logic"""

# -- importing modules
from .flask_shortcuts import initialize_app

def create_app():
    initialize_app.create_app()
