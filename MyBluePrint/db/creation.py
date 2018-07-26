from datetime import datetime
from . import db
from ..models import User
from flask import current_app

def SeedAll():
    CreateTables()
    SeedUsers()

def CreateTables():
    from sqlalchemy import MetaData
    metadata = MetaData()
    metadata.reflect(db.get_engine(bind='default'))
    if 'user' not in metadata.tables.keys():
        print('Creating Tables')
        db.create_all(bind='default')

def SeedUsers():
    u = User.query.filter_by(email='user@demo.com').first()
    if u is None:
        print('Creating Users')
        from Auth.Hashing import hash_password
        password = current_app.config['DEFAULT_SQLALCHEMY_PASSWORD']
        pw_hash = hash_password('user@demo.com', password)
        u = User('user@demo.com')
        u.pw_hash = pw_hash
        u.created = datetime.today()
        db.session.add(u)
        db.session.commit()