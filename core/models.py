"""- Database initialization
-- users table"""

# -- importing modules
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
socketio = None


# -- users table
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    password_sha256 = db.Column(db.String(256), nullable=False)

    username = db.Column(db.String(32), nullable=False)
    privileges = db.Column(db.Integer, default=0)

    elo = db.Column(db.Integer, default=1000)
