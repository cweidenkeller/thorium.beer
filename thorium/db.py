from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_db():
    from thorium.app import app
    db = SQLAlchemy(app)
    db.create_all()


def get_db():
    from thorium.app import app
    db = SQLAlchemy(app)
    return db
