from main import db
import sqlite3

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    msg = db.Column(db.Text())

    def __init__(self, name, email, msg):
        self.name = name
        self.email = email
        self.msg = msg

class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    state = db.Column(db.String(200))
    city = db.Column(db.String(200))
    password = db.Column(db.String(100))

    def __init__(self, name, email, state, city, password):
        self.name = name
        self.email = email
        self.state = state
        self.city = city
        self.password = password

    
class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.Text())

    def __init__(self,email, msg):
        self.email = email
        self.msg = msg