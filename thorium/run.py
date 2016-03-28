from flask import Flask, Blueprint
from thorium.site import site

app = Flask(__name__)
FAVICON_URL=('http://dd58d482324888e2ee02-a7b127e0d8b7487c5933cbe965f92cbd.'
            'r61.cf1.rackcdn.com/favicon.ico')

@app.errorhandler(404)
def page_not_found(error):
    return "PAGE NOT FOUND", 404

@app.route('/favicon.ico', methods=['GET'])
    def favicon():
        return redirect(FAVICON_URL)

def run():
    app.add
    app.register_blueprint(site)
    app.debug = False
    app.run(host='0.0.0.0', port=80)

