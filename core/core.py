"""- Core functions, and overall app logic"""

# -- importing modules
from werkzeug.security import generate_password_hash, check_password_hash
import settings
from core.logger import log


def create_app(name):
    from .flask_shortcuts import initialize_app
    return initialize_app.create_app(name)


def create_admin_user():
    register_user(settings.ADMIN_USERNAME, settings.ADMIN_PASSWORD, permission_group=settings.ADMIN_PERMISSION_GROUP,
                  elo=settings.ADMIN_ELO, email=settings.ADMIN_EMAIL)


def register_user(username, password, email, elo=settings.DEFAULT_ELO,
                  permission_group=settings.DEFAULT_PERMISSION_GROUP):
    from .models import User, db

    does_username_exist = User.query.filter_by(username=username).count()

    if does_username_exist > 0:
        return

    user = User(
        username=username,
        password=generate_password_hash(password),
        permission_group=permission_group,
        elo=elo,
        email=email
    )

    db.session.add(user)
    db.session.commit()
    log.info(f'Created user: {username}')

    return user


def check_credentials(username, password):
    from .models import User, db

    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    if check_password_hash(user.password, password):
        return True

    return False
