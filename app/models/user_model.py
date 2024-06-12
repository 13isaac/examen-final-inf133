from app.database import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
import json

class User(db.Model,UserMixin):
    __tablename__="users"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(50), nullable=False, unique=True)
    password=db.Column(db.String(128), nullable=False)
    phone=db.Column(db.String(50), nullable=False)
    role=db.Column(db.String(50), nullable=False)

    def __init__(self,name,email,password,phone,role=["customer"]):
        self.name=name
        self.email=email
        self.password=password
        self.phone=phone
        self.role=json.dumps(role)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
    
