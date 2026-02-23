"""- Flask app initialization script"""

from flask import Flask
import settings
from core.models import db, User
from flask_socketio import SocketIO
import core
import os
import sys
import settings


# - app initialization
def create_app() -> Flask:
    app = Flask(__name__)

    config_class = CONFIGS.get(config_name)
    app.config.from_object(config_class)

    db.init_app(app)
    socketio = SocketIO(app)

    with app.app_context():
        from blueprints.main.routes import bp as main_bp
        from core import context_precessors

        for context_processor in context_precessors.context_processors:
            app.context_processor(context_processor)

        app.before_request(load_user)

        app.register_blueprint(main_bp)

        db.create_all()

        if not User.query.filter_by(username=app.config['DEFAULT_ADMIN_USERNAME']).first():
            admin_user = User(
                username=app.config['DEFAULT_ADMIN_USERNAME'],
                password_sha256=hash_password(app.config['DEFAULT_ADMIN_PASSWORD']),
                privileges=1,
                elo=app.config['DEFAULT_ELO']
            )

            db.session.add(admin_user)
            db.session.commit()

    def render_markdown(text):
        html = markdown.markdown(
            text,
            extensions=[
                "fenced_code",
                "codehilite",
                "tables",
                "nl2br",
                "sane_lists"
            ]
        )
        return Markup(html)

    app.jinja_env.filters["markdown"] = render_markdown

    return app

return