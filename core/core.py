"""- Core functions, and overall app logic"""

# -- importing modules
from werkzeug.security import generate_password_hash
import settings
import flask


def create_app(name):
    from .flask_shortcuts import initialize_app
    return initialize_app.create_app(name)


def create_admin_user():
    from .models import User, db

    admin_users_count = User.query.filter_by(permission_group=settings.ADMIN_USERNAME).count()

    if admin_users_count > 0:
        return

    admin = User(
        username=settings.ADMIN_USERNAME,
        password=generate_password_hash(settings.ADMIN_PASSWORD),
        permission_group="admin",
        elo=settings.ADMIN_ELO
    )

    db.session.add(admin)
    db.session.commit()

    return admin