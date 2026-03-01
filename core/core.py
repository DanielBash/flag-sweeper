"""- Core functions, and overall app logic"""

# -- importing modules
from werkzeug.security import generate_password_hash, check_password_hash
from core.models import MailMessage
import settings
from core.logger import log
import docker


def create_app(name):
    from .flask_shortcuts import initialize_app
    return initialize_app.create_app(name)


def create_admin_user():
    register_user(settings.ADMIN_USERNAME, settings.ADMIN_PASSWORD, permission_group=settings.ADMIN_PERMISSION_GROUP,
                  elo=settings.ADMIN_ELO, email=settings.ADMIN_EMAIL, bio=settings.ADMIN_BIO, status=settings.ADMIN_STATUS)


def register_user(username, password, email, elo=settings.DEFAULT_ELO,
                  permission_group=settings.DEFAULT_PERMISSION_GROUP, status=settings.DEFAULT_STATUS, bio=settings.DEFAULT_BIO):
    from .models import User, db

    does_username_exist = User.query.filter_by(username=username).count()

    if does_username_exist > 0:
        return

    user = User(
        username=username,
        password=generate_password_hash(password),
        permission_group=permission_group,
        elo=elo,
        email=email,
        bio=bio,
        status=status
    )

    db.session.add(user)
    db.session.commit()
    
    welcome_message = MailMessage(
        subject='Welcome email!',
        receiver_id=user.id,
        sender_id=User.query.filter_by(username=settings.ADMIN_USERNAME).first().id,
        content='Welcome to flag sweeper! Nice to meet you in our community. Explore endless possabilities!'
    )
    db.session.add(welcome_message)
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


def create_user_container(user_id: int):
    container = settings.CLIENT.containers.run(
        "ubuntu:latest",
        command="/bin/bash",
        stdin_open=True,
        tty=True,
        detach=True,
        name=f"user-{user_id}",
        labels={
            "managed": "true",
            "user_id": str(user_id),
            "type": "flag_sweeper_container"
        },
        mem_limit="512m",
        nano_cpus=1_000_000_000,
        pids_limit=128,
        security_opt=["no-new-privileges"],
        remove=False
    )
    
    return container


def remove_left_containers():
    containers = settings.CLIENT.containers.list(
        all=True,
        filters={"label": "type=myhosting"}
    )

    for container in containers:
        log.info(f'Removing container: {container.name}')
        container.remove(force=True)