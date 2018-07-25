from .db import db

class User(db.Model):
    __bind_key__ = 'default'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(120), unique=True)
    pw_hash = db.Column(db.Unicode(80))
    logins = db.Column(db.Integer, server_default="0")
    last_login = db.Column(db.DateTime)
    created = db.Column(db.DateTime)

    def __init__(self, email):
        self.email = email
    def __repr__(self):
        return '<User %r>' % self.email
