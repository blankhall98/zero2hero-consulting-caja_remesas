from app.extensions import db
from datetime import datetime
from flask_login import UserMixin
import enum

class Role(enum.Enum):
    admin = 'admin'
    super = 'super'
    user = 'user'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum(Role), default=Role.user, nullable=False)
    origin = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<User {self.username}>'

