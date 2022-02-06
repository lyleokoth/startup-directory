from tkinter import S
from app import app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from app import db
from app.models import StartUp
from flask import jsonify

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
def dashboard_page():
    return render_template('dashboard_page.html')

def get_startups():
    startups = {}
    searches = StartUp.query.all()[:10]
    for startup in searches:
        startups[startup.id] = {
            'Startup Name': startup.startup_name,
            'Startup Description' : startup.startup_description
        }
    return startups


@app.route('/startups', methods=['GET'])
def startups_page():
    #startups = get_startups()
    page_number = request.args.get('page', 1, type=int)
    #startups = StartUp.query
    results = StartUp.query.paginate(page=page_number, per_page=app.config['RESULTS_PER_PAGE'])
    startups = []
    for result in results.items:
        startups.append(
            {
                'id': result.id,
                'startup_name': result.startup_name,
                'startup_description': result.startup_description,
                'startup_website': result.startup_website
            }
        )
    return render_template('startups_page.html', startups=startups)

@app.route('/data', methods=['GET'])
def data():
    results = {}
    searches = StartUp.query.all()
    for startup in searches:
        results[startup.id] = {
            'Startup Name': startup.startup_name,
            'Startup Description' : startup.startup_description
        }
    return jsonify(results)

@app.route('/investors', methods=['GET'])
def investor_page():
    return render_template('investors_page.html')

@app.route('/business_hubs', methods=['GET'])
def business_hubs_page():
    return render_template('business_hubs_page.html')

