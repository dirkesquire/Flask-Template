export FLASK_APP=start.py
export FLASK_DEBUG=1
flask shell

#Doing 'flask shell' is perferred to python -i start.py because an app_context is always in effect.