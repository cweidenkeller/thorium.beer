from flask import Flask, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from thorium.site import site

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/thorium/thorium.db'
db = SQLAlchemy(app)
from thorium.site import site
app.register_blueprint(site)

@app.errorhandler(404)
def page_not_found(error):
    return "PAGE NOT FOUND", 404
