from tests.base import BaseTest
from app.models import db, User, to_dict


class FunctionTest(BaseTest):

    def test_to_dict_function_for_user_instance(self):
        user = User(
            names='Yami',
            last_names='Orejuela',
            address='CRA 1 #88-99',
            phone_numbers='3264568,4569885'
        )
        db.session.add(user)
        db.session.commit()

        user_dict = to_dict(User)
        self.assertIsInstance(user_dict, dict)
