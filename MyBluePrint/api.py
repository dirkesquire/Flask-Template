from flask import Flask, jsonify, abort, make_response, request, url_for, redirect
from . import app
from .db import db
from .models import User

rootApi = "/api/v1.0/"
fruits = ['Apples', 'Bananas', 'Pears', 'Oranges']

@app.route('/api/')
def api_root():
    return redirect(url_for('.what_can_i_do'), code=302)

@app.route(rootApi)
def what_can_i_do():
    urls = {
        '1. help': [
            {
                'urn': url_for('.what_can_i_do', _external=True),
                'title': u'GET help (this document)',
            },
        ],
        '2. interface': [
            {
                'urn:': url_for('.api_fruits', _external=True),
                'title': u'GET Fruits | POST new Fruit',
            },
        ]
    }

    return jsonify(urls)

@app.route(rootApi + 'fruits', methods=['GET', 'POST'])
def api_fruits():
    """
    Get a list of fruits, or add a new one
    """
    if request.method == 'GET':
        return jsonify(fruits)
    elif request.method == 'POST':
        """
        To test this try posting the following json: {"fruits": ["Cherry"]}
        Remember to send as application/json.
        """
        data = request.get_json()
        fruits.extend(data.get('fruits'))
        return jsonify({'success': True, 'Method': request.method, 'fruits': fruits, 'IsJson': request.is_json, 'form': request.form})


