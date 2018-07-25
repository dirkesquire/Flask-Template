import os, sys
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
app.config.from_pyfile('settings.local.cfg', silent=True)

from MyBluePrint import app as myblueprint
app.register_blueprint(myblueprint, url_prefix='/myblueprint')

# A blue print can be registered multiple times at different urls.
# Here we register the same blueprint on the root.
from MyBluePrint import app as myblueprint
app.register_blueprint(myblueprint, url_prefix='/')

from RestJS import app as restjs
app.register_blueprint(restjs, url_prefix='/restjs')

# Init ASQLAlchemy for MyBluePrint
with app.app_context():
    from MyBluePrint.db import db, init_sqlalchemy
    init_sqlalchemy(app)

@app.shell_context_processor
def make_shell_context():
    # Locals available in `flask shell`:
    from MyBluePrint.db import db
    from MyBluePrint.db.creation import CreateTables, SeedAll, SeedUsers
    from MyBluePrint.models import User  #, ... add others here
    from sqlalchemy import MetaData
    metadata = MetaData()
    metadata.reflect(db.get_engine(bind='default'))
    return { 'db': db, 'metadata': metadata, 'User': User, 'CreateTables': CreateTables, 'SeedAll': SeedAll }

# Print_ all Routes
if len(sys.argv) > 1:
    if sys.argv[1] == 'map':
        print(app.url_map)

if __name__ == "__main__":
    #If we enter using 'python start.py' we need app.run. If we run with 'flask run' then we do not.
    app.run(debug=True, port=5000, threaded=True)
    # app.run(debug=True, port=80, threaded=True, host="mymachinename")
    # threaded: is not default and needed to make internal api http requests
