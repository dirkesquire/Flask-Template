# Flask-Template
Get started quickly using Flask!

The following files contain many of the basics to get going with flask.


## To get started run:
```
. env-install
. shell.sh
>>> SeedAll()            #This creates the database
>>> exit
. start.sh
```

Then visit the site at http://127.0.0.1:5000/myblueprint.

The general idea is two pages:
Home page:
    Anonymous access
Private page:
    Need to login first. Provided you have created the database, the default login is:
    username: user@demo.com
    password: demo


Tests
-------
I provide an example of running tests. This is triggered with the following script:
```. test.sh```

Blueprints
----------
For larger apps, blueprints are a super convenient way to go. In the Flask tutorials these can sound daunting, but this sample code shows just how easy it is to achieve. Flask blueprints are similar in nature to Django apps, so you can have more than one per website.

## For further flask information:
---------
http://flask.pocoo.org
