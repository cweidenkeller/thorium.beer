from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

create_db():
    from thorium.app import app
    db = SQLAlchemy(app)
    db.create_all()
