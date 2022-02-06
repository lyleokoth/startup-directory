from flask import Flask
from app.config import DevelopmentConfig, ProductionConfig, DATA_URL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

from app import routes, models

def x(startup):
    s = models.StartUp(startup_name=startup['team_name'], 
    startup_description=startup['startup_idea'], startup_website=startup['leader_name'])
    return s

def populate_startups_table():
    startups = os.path.join(DATA_URL, 'botswana_startups.json')
    with open(startups, 'r') as f:
        all_startups = json.load(f)
        for startup in all_startups:
            s = x(startup)
            db.session.add(s)
        db.session.commit()

@app.before_first_request
def initialize_database():
    models.db.create_all()
    #populate_startups_table()