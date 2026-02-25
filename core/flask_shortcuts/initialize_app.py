""" - Flask app initialization script"""

from flask import Flask
import settings
from ..models import db, User
from flask_socketio import SocketIO
import core
import os
import sys
import settings
from . import context_processors
from . import before_request
from . import jinja_filters
from . import after_initialization
from ..logger import log


# - app initialization
def create_app(name) -> Flask:
    app = Flask(name)

    app.config.from_object(settings.FLASK_SETTINGS)

    db.init_app(app)
    socketio = SocketIO(app)

    log.info('Initializing blueprints')
    with app.app_context():
        from blueprints import blueprints

        for context_processor in context_processors.context_processors:
            app.context_processor(context_processor)

        for before_request_func in before_request.before_request:
            app.before_request(before_request_func)

        for bp in blueprints:
            if bp not in settings.BASE_BLUEPRINTS:
                app.register_blueprint(blueprints[bp], url_prefix=f'/{bp}')
            else:
                app.register_blueprint(blueprints[bp])

        db.create_all()

        after_initialization.main()

    for key, val in jinja_filters.jinja_filters.items():
        app.jinja_env.filters[key] = val

    return app