import os
import importlib
from flask import Blueprint

from core.logger import log

blueprints = {}

current_dir = os.path.dirname(os.path.abspath(__file__))

for item in os.listdir(current_dir):
    folder_path = os.path.join(current_dir, item)
    if (os.path.isdir(folder_path) and
            os.path.exists(os.path.join(folder_path, '__init__.py')) and
            os.path.exists(os.path.join(folder_path, 'routes.py'))):

        try:
            routes_module = importlib.import_module(f'.{item}.routes', package=__package__)
            if hasattr(routes_module, 'bp') and isinstance(routes_module.bp, Blueprint):
                blueprints[item] = routes_module.bp
        except ImportError:
            pass
log.info(blueprints.keys())
