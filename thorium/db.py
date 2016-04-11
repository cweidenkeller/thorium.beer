from thorium.app import db

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_name = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(32))
    style = db.Column(db.String(32))
    description = db.Column(db.String(1024))
    abv = db.Column(db.Float)
    srm = db.Column(db.Float)
    ibu = db.Column(db.Float)
    beer_img_url = db.Column(db.String(1024))
    logo_url = db.Column(db.String(1024))

    def __init__(self, name, style, description, abv,
                 srm, ibu, beer_img_url, logo_url):
        self.name = name
        self.style = style
        self.description = description
        self.abv = abv
        self.srm = srm
        self.ibu = ibu
        self.beer_img_url = beer_img_url
        self.logo_url = logo_url

    def __repr__(self):
        return '<Beer {0}'.format(self.name)

