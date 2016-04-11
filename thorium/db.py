from thorium.app import db

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_name = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(32))
    style = db.Column(db.String(32))
    abv = db.Column(db.Float)
    ibu = db.Column(db.Float)
    srm = db.Column(db.Float)
    description = db.Column(db.String(1024))

    def __init__(self, url_name, name, style, abv, ibu, srm, description):
        self.url_name = url_name
        self.name = name
        self.style = style
        self.description = description
        self.abv = abv
        self.ibu = ibu
        self.srm = srm

    def __repr__(self):
        return '<Beer {0}'.format(self.name)

