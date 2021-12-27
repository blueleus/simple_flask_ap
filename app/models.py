from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def to_dict(row):
    return {column.name: getattr(row, row.__mapper__.get_property_by_column(column).key) for column in row.__table__.columns}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(255), nullable=False)
    last_names = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_numbers = db.Column(db.String(255))
