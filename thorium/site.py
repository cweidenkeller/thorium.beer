from flask import Blueprint, render_template, redirect, abort
from thorium.db import Beer

site = Blueprint('thorium', __name__,
                 template_folder='templates')

@site.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@site.route('/beer/<url_name>', methods=['GET'])
def beer(url_name):
    beer = Beer.query.filter_by(url_name=url_name).first_or_404()
    return render_template('beer.html', name=beer.name, style=beer.style,
                           abv=beer.abv, ibu=beer.ibu, srm=beer.srm,
                           description=beer.description)

@site.route('/about_us', methods=['GET'])
def about_us():
    return render_template('about_us.html')

@site.route('/contact_us', methods=['GET'])
def contact_us():
    return render_template('contact_us.html')

@site.route('/survey', methods=['GET'])
def survey():
    return redirect('https://www.surveymonkey.com/r/2W9XQDK',
                    code=301)

@site.route('/facebook', methods=['GET'])
def facebook():
    return redirect('https://www.facebook.com/thorium.beer/',
                    code=301)
