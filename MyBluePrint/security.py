from flask import Flask, jsonify, abort, make_response, request, url_for, render_template, redirect, session, flash
from Auth.HttpSessionAuth import HTTPSessionAuth
from Auth.Hashing import hash_password
from datetime import datetime
from . import app
from .db import db
from .models import User
auth = HTTPSessionAuth()

ROOTURI = "/"
LOGIN_REDIRECT = '.home'
LOGOUT_REDIRECT = '.login'

@auth.error_handler
def auth_error():
    print('Access Denied')
    return redirect(url_for('.login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    print('Finance.Login')
    error = None
    username = request.form.get('username') or ''
    if request.method == 'POST':
        password = request.form['password']
        pw_hash = hash_password(username, password)

        if username is None:
            error = 'Email address required'
        elif password is None:
            error = 'Password is required'
        else:
            user = User.query.filter_by(email=username).first()
            if (user is None):
                error = 'User not found'
            elif (user.pw_hash != pw_hash):
                error = 'Wrong password'
            else:
                session['logged_in'] = True
                flash('You were logged in')
                user.logins = (user.logins or 0) + 1
                user.last_login = datetime.today()
                db.session.commit()
                return redirect(url_for(LOGIN_REDIRECT))
    return render_template('MyBluePrint/login.html', error=error, username=username)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for(LOGOUT_REDIRECT))