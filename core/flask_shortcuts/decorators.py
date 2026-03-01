""" - Decorators for flask views"""

# -- importing modules
from functools import wraps
from flask import g, abort, redirect, url_for
import settings


def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view_func(*args, **kwargs)
    return wrapper


def required_permissions(*permissions):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if g.user is None:
                abort(401)
            
            perms = settings.PERMISSION_GROUPS[g.user.permission_group]
            if not all(p in perms for p in permissions):
                abort(403)

            return view_func(*args, **kwargs)
        return wrapper
    return decorator