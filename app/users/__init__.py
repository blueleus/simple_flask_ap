from flask import Blueprint, jsonify, request
from app.models import db, User, to_dict

users = Blueprint('users', __name__, url_prefix='/user')


@users.route('', methods=('POST',))
def create():
    user = User(
        names=request.form['names'],
        last_names=request.form['last_names'],
        address=request.form['address'],
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.id)


@users.route('', defaults={'user_id': None})
@users.route('/<int:user_id>')
def get(user_id):
    if user_id:
        user = User.query.get(user_id)
        return jsonify(to_dict(user))
    else:
        rows = User.query.all()
        user_list = [to_dict(row) for row in rows]
        return jsonify(user_list)
