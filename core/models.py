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
    
    # - hidden data
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(256), nullable=False)
    permission_group = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    sent_messages = db.relationship(
        "MailMessage",
        foreign_keys="MailMessage.sender_id",
        backref="sender",
        lazy="dynamic"
    )

    received_messages = db.relationship(
        "MailMessage",
        foreign_keys="MailMessage.receiver_id",
        backref="receiver",
        lazy="dynamic"
    )
    
    posts = db.relationship(
        "Post",
        foreign_keys="Post.user_id",
        backref="author",
        lazy="dynamic"
    )
    
    
    # - public info
    username = db.Column(db.String(32), nullable=False, unique=True, index=True)
    bio = db.Column(db.String(5000), nullable=False, default='')
    elo = db.Column(db.Integer, default=1000)
    status = db.Column(db.String(30), nullable=False, default='')
    registered_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def get_permission(self, name):
        permissions = settings.PERMISSION_GROUPS[self.permission_group]

        if name not in permissions:
            return None
        else:
            return permissions[name]
    
    @property
    def get_recieved_mail_messages(self):
        return self.received_messages.order_by(
            MailMessage.sent_at.desc()
        ).all()

    @property
    def get_sent_mail_messages(self):
        return self.sent_messages.order_by(
            MailMessage.sent_at.desc()
        ).all()


# -- mail messages table
class MailMessage(db.Model):
    __tablename__ = "mail_messages"
    
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True)
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True)
    
    content = db.Column(db.Text, nullable=False)
    subject = db.Column(db.String(30), nullable=False)
        
    sent_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
    
    @property
    def sender_user(self):
        return User.query.filter_by(id=self.sender_id).first()
    
    @property
    def receiver_user(self):
        return User.query.filter_by(id=self.receiver_id).first()


# -- posts table
class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer, db.ForeignKey("users.id"), index=True)
    
    content = db.Column(db.Text, nullable=False)
    subject = db.Column(db.String(30), nullable=False)
    
    published_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )