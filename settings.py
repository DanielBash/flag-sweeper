"""- Project-wide settings initialization"""


# - importing modules
import dotenv
import importlib
import os
from core.logger import log


# -- loading settings template
dotenv.load_dotenv()
settings_template = os.environ.get('SETTINGS_TEMPLATE', 'settings_templates.default')
if not settings_template.startswith('settings_templates.'):
    settings_template = 'settings_templates.' + settings_template

module = importlib.import_module(settings_template)

for key in dir(module):
    if key.isupper():
        globals()[key] = getattr(module, key)

# -- loading env variables
globals().update({
    k: v for k, v in os.environ.items()
    if k.isupper()
})


# -- creating flask settings object
class FlaskSettings:
    def __init__(self):
        for key, value in globals().items():
            if key.isupper():
                setattr(self, key, value)


FLASK_SETTINGS = FlaskSettings()

# -- settings initialization log
if PRINT_CONSTANTS and os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    log.info('Loaded settings. Listing:')
    for i in dir(module):
        if i.isupper():
            log.rich(f'[red]{i}[/] = {globals()[i]}')
