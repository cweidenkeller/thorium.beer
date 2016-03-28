from flask import Blueprint, render_template


site = Blueprint('thorium', __name__,
                 template_folder='templates')

@site.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@site.route('/beer/<beer_name>', methods=['GET'])
def beer(beer_name):
    return render_template('beer.html', beer_name=beer_name)

@site.route('/about_us', methods=['GET'])
def about_us():
    return render_template('about_us.html')
