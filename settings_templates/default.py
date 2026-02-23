"""- Default settings template"""

# -- importing modules
from pathlib import Path

# -- flask settings
PORT = 8080
HOST = '0.0.0.0'
SECRET_KEY = 'unsecure-secret-key'

# -- app settings
DEBUG = False
PRINT_CONSTANTS = True

# -- sqlalchemy database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
TEMPLATE_PATH = Path('templates')