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


# - app initialization
def create_app(name) -> Flask:
    app = Flask(name)

    app.config.from_object(settings.FLASK_SETTINGS)

    db.init_app(app)
    socketio = SocketIO(app)

    with app.app_context():
        from blueprints.main.routes import bp as main_bp

        for context_processor in context_processors.context_processors:
            app.context_processor(context_processor)

        for before_request_func in before_request.before_request:
            app.before_request(before_request_func)

        app.register_blueprint(main_bp)

        db.create_all()

    for key, val in jinja_filters.jinja_filters.items():
        app.jinja_env.filters[key] = val

    return app