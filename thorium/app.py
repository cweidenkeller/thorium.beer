from flask import Flask, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from thorium.site import site
from thorium.db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/thorium/thorium.db'
app.register_blueprint(site)

@app.errorhandler(404)
def page_not_found(error):
    return "PAGE NOT FOUND", 404
db.init_app(app)
db.app = app
db.create_all()
