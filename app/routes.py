from app import app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
def dashboard_page():
    return 'Hello from flask'

