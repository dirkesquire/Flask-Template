#!/usr/bin/python

activate_this='/var/www/Flask-Template/env/bin/activate_this.py'
execfile(activate_this,dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Flask-Template/")

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
app.config.from_pyfile('settings.local.cfg', silent=True)

from RestJS import app as restjs
app.register_blueprint(restjs, url_prefix='/restjs')

from MyBluePrint import app as myblueprint
app.register_blueprint(myblueprint, url_prefix='/myblueprint')

# Init ASQLAlchemy for MyBluePrint
with app.app_context():
    from MyBluePrint.db import db, init_sqlalchemy
    init_sqlalchemy(app)

application = app
