"""- Project-wide settings initialization"""

# - importing modules
import dotenv
import os

# -- loading settings template
dotenv.load_dotenv()
settings_template = os.environ.get('SETTINGS_TEMPLATE', 'default_settings')
__import__(settings_template)
