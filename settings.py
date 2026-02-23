"""- Project-wide settings initialization"""

# - importing modules
import dotenv
import os
import importlib
import builtins
from core.logger import log


# -- loading settings template
dotenv.load_dotenv()
settings_template = os.environ.get('SETTINGS_TEMPLATE', 'settings_templates.default_settings')

module = importlib.import_module(settings_template)

for key in dir(module):
    if key.isupper():
        globals()[key] = getattr(module, key)


# -- loading env variables
globals().update({
    k: v for k, v in os.environ.items()
    if k.isupper()
})


log.info('Loaded settings. Listing:')
if PRINT_CONSTANTS:
    for i in dir(module):
        if i.isupper():
            log.rich(f'[red]{i}[/] = {globals()[i]}')
