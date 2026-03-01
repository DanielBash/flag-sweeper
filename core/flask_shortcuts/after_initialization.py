""" - Code running after app initialization
 - Final setup"""


# -- importing modules
import settings
from flask import current_app
from .. import models
from core.core import create_admin_user, remove_left_containers
from core.logger import log


def main():
    log.info('Creating admin user')
    create_admin_user()
    log.info('Checking for app containers left')
    remove_left_containers()


if __name__ == '__main__':
    main()
