from tests.base import BaseTest
from sqlalchemy.exc import IntegrityError
from app.models import db, User


class ModelTest(BaseTest):
    def test_user_names_is_required(self):
        with self.assertRaises(IntegrityError):
            user = User()
            db.session.add(user)
            db.session.commit()

    def test_user_last_names_is_required(self):
        with self.assertRaises(IntegrityError):
            user = User(names='User')
            db.session.add(user)
            db.session.commit()

    def test_user_address_is_required(self):
        with self.assertRaises(IntegrityError):
            user = User(
                names='User',
                last_names='Uno'
            )
            db.session.add(user)
            db.session.commit()

    def test_create_user_with_basic_data(self):
        user = User(
            names='Yami',
            last_names='Orejuela',
            address='CRA 1 #88-99',
            phone_numbers='3264568,4569885'
        )
        db.session.add(user)
        db.session.commit()

        users = User.query.all()
        self.assertEqual(len(users), 1)

    def test_user_id_is_unique(self):
        user_1 = User(
            names='Yami',
            last_names='Orejuela',
            address='CRA 1 #88-99',
            phone_numbers='3264568,4569885'
        )

        user_2 = User(
            names='Yami',
            last_names='Orejuela',
            address='CRA 1 #88-99',
            phone_numbers='3264568,4569885'
        )

        db.session.add(user_1)
        db.session.add(user_2)
        db.session.commit()

        self.assertNotEqual(user_1.id, user_2.id)
