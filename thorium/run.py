from flask import Flask, Blueprint
from thorium.site import site

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return "PAGE NOT FOUND", 404



def run():
    app.register_blueprint(site)
    app.debug = False
    app.run(host='0.0.0.0', port=80)

