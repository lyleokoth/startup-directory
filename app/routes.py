from app import app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
def dashboard_page():
    return render_template('dashboard_page.html')

@app.route('/startups', methods=['GET'])
def startups_page():
    return render_template('startups_page.html')

@app.route('/investors', methods=['GET'])
def investor_page():
    return render_template('investors_page.html')

@app.route('/business_hubs', methods=['GET'])
def business_hubs_page():
    return render_template('business_hubs_page.html')

