"""- Default settings template"""

# -- importing modules
from pathlib import Path

# -- flask settings
PORT = 8080  # running port
HOST = '0.0.0.0'  # on what host to run app
SECRET_KEY = 'unsecure-secret-key'  # app secret key for cryptography. sessions, for example

# -- app settings
DEBUG = False  # is app run in debug mode?
PRINT_CONSTANTS = True  # do we need to print settings when initializing?

# -- sqlalchemy database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # database connection uri
TEMPLATE_PATH = Path('templates')  # templates folder path

# -- blueprints settings
BASE_BLUEPRINTS = ['main', 'index']  # blueprints that can be handled without url prefix

# -- permissions settings
PERMISSION_GROUPS = {
    'admin': {
        'MAX_CONTAINER_RAM_SIZE_MB': 500,
        'MAX_CONTAINER_SIZE_MB': 1000,
        'MAX_CONTAINER_PROCESSES': 5000,
        'MAX_CONTAINER_LIFETIME_MINUTES': 60 * 24,
        'VIEW_ADMIN_PANEL': True
    },
    'user': {
        'MAX_CONTAINER_RAM_SIZE_MB': 120,
        'MAX_CONTAINER_SIZE_MB': 300,
        'MAX_CONTAINER_PROCESSES': 64,
        'MAX_CONTAINER_LIFETIME_MINUTES': 60,
        'VIEW_ADMIN_PANEL': False
    }
}

DEFAULT_PERMISSION_GROUP = 'user'

# -- admin credentials
ADMIN_PASSWORD = 'password'
ADMIN_USERNAME = 'admin'
ADMIN_PERMISSION_GROUP = 'admin'
ADMIN_ELO = 1000
