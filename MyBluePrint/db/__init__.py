# -*- coding: utf-8 -*-
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_sqlalchemy(app):
    db.init_app(app)