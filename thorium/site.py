from flask import Blueprint, render_template, redirect


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

@site.route('/survey', methods=['GET'])
def survey():
    return redirect('https://www.surveymonkey.com/r/2W9XQDK',
                    code=301)
