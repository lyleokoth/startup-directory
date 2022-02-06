from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StartUp(db.Model):
    __tablename__ = 'startups'

    id = db.Column(db.Integer, primary_key=True)
    startup_name = db.Column(db.String(64), unique=True)
    startup_description = db.Column(db.String(120))
    startup_website = db.Column(db.String(120))

    def __init__(self, startup_name, startup_description, startup_website):
        self.startup_name = startup_name
        self.startup_description = startup_description
        self.startup_website = startup_website

class Investor(db.Model):
    __tablename__ = 'investors'

    id = db.Column(db.Integer, primary_key=True)
    investor_name = db.Column(db.String(64), unique=True)
    investor_description = db.Column(db.String(120))
    investor_website = db.Column(db.String(120))

    def __init__(self, investor_name, investor_description, investor_website):
        self.investor_name = investor_name
        self.investor_description = investor_description
        self.investor_website = investor_website

class Hub(db.Model):
    __tablename__ = 'hubs'
    
    id = db.Column(db.Integer, primary_key=True)
    hub_name = db.Column(db.String(64), unique=True)
    hub_description = db.Column(db.String(120))
    hub_website = db.Column(db.String(120))

    def __init__(self, hub_name, hub_description, hub_website):
        self.hub_name = hub_name
        self.hub_description = hub_description
        self.hub_website = hub_website