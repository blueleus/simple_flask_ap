from flask_testing import TestCase
from app import create_app
from app.models import db
import os
import json


class BaseTest(TestCase):
    TESTING = True
    DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test.sqlite")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

    def create_app(self):
        return create_app(self)

    def setUp(self) -> None:
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def is_json(self, my_json):
        try:
            json_object = json.loads(my_json)
        except ValueError as e:
            return False
        return True
