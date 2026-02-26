"""- Database initialization
-- Users table"""

# -- importing modules
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.mutable import MutableDict
import settings


db = SQLAlchemy()
socketio = None


# -- users table
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(256), nullable=False)

    username = db.Column(db.String(32), nullable=False)
    permission_group = db.Column(db.String(32), nullable=False)

    elo = db.Column(db.Integer, default=1000)

    email = db.Column(db.String(256), nullable=False)

    def get_permission(self, name):
        permissions = settings.PERMISSION_GROUPS[self.permission_group]

        if name not in permissions:
            return None
        else:
            return permissions[name]
