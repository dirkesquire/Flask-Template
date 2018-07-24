import os, sys
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

@app.shell_context_processor
def make_shell_context():
    # Locals available in `flask shell`:
    from MyBluePrint.db import db
    from MyBluePrint.models import User  #, ... add others here
    from sqlalchemy import MetaData
    metadata = MetaData()
    metadata.reflect(DB.get_engine(bind='finance'))
    return { 'db': db, 'metadata': metadata, 'User': User, 'CreateTables': CreateTables, 'SeedAll': SeedData }

# Print_ all Routes
if len(sys.argv) > 1:
    if sys.argv[1] == 'map':
        print(app.url_map)

if __name__ == "__main__":
    #If we enter using 'python start.py' we need app.run. If we run with 'flask run' then we do not.
    app.run(debug=True, port=5000, threaded=True)
    # app.run(debug=True, port=80, threaded=True, host="mymachinename")
    # threaded: is not default and needed to make internal api http requests
