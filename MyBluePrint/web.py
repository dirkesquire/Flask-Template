from flask import Flask, jsonify, abort, make_response, request, url_for, render_template, redirect
from . import app, auth

@app.route('/')
def root():
    return redirect(url_for('.home'), code=302)

@app.route('/home')
def home():
    example = request.args.get('example') or 'Example text'
    return render_template('MyBluePrint/home.html', example=example)

@app.route('/private')
@auth.login_required
def private():
    example = request.args.get('example') or 'Example text'
    return render_template('MyBluePrint/private.html', example=example)

@app.route("/home/hello")
def hello():
    return "Hello World!"

@app.route('/home/brython')
def brython_demo():
    """ BRYTHON DEMO """
    return render_template('MyBluePrint/brython_demo.html')

