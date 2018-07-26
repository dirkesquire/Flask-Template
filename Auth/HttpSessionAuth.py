"""
flask_httpauth
==================

This module extend's Miguel Grinberg's flask_httpauth library to offer session authentication

:copyright: (C) 2017 by Dirk Roeleveld
:license:   MIT, see LICENSE for more details.
"""

from flask_httpauth import HTTPAuth
from functools import wraps
from flask import request, make_response, session, flash, redirect, url_for

__version__ = '1.0.0'

class HTTPSessionAuth(HTTPAuth):
    LOGGING = False

    def __init__(self, scheme=None, realm=None):
        super(HTTPSessionAuth, self).__init__(scheme or 'Session', realm)

    def login_required(self, f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                self.log('Session authenticated (web): OK')
                return f(*args, **kwargs)
            else:
                self.log('Session authenticated (web): Fail')
                return self.auth_error_callback()
        return wrap

    def logged_in(self):
        return 'logged_in' in session

    def perform_login(self, username):
        session['logged_in'] = True
        session['username'] = username

    def perform_logout(self):
        session.pop('logged_in', None)
        session.pop('username', None)

    def username(self):
        return session.get('username')

    def log(self, message):
        if self.LOGGING:
            print(message)
