from tests.base import BaseTest
from app.models import User
import json


class ViewTest(BaseTest):
    def test_POST_user_returned_200(self):
        response = self.client.post('/user', data={
            'names': 'user',
            'last_names': 'uno',
            'address': 'CRA 1 #99-88',
        })
        self.assertStatus(response, 200)

    def test_POST_user_returned_numeric_id(self):
        response = self.client.post('/user', data={
            'names': 'user',
            'last_names': 'uno',
            'address': 'CRA 1 #99-88',
        })
        self.assertIsInstance(int(response.data), int)

    def test_POST_user_returned_user_id(self):
        response = self.client.post('/user', data={
            'names': 'user',
            'last_names': 'uno',
            'address': 'CRA 1 #99-88',
        })
        user = User.query.filter_by(id=int(response.data)).first()
        self.assertIsNotNone(user)

    def test_POST_user_returned_correct_user_id(self):
        response1 = self.client.post('/user', data={
            'names': 'user1',
            'last_names': 'uno',
            'address': 'CRA 1 #99-88',
        })
        response2 = self.client.post('/user', data={
            'names': 'user2',
            'last_names': 'dos',
            'address': 'CRA 2 #99-88',
        })

        user_id1 = int(response1.data)
        user_id2 = int(response2.data)
        self.assertNotEqual(user_id1, user_id2)

    def test_GET_user_returned_200(self):
        response = self.client.get('/user')
        self.assertStatus(response, 200)

    def test_GET_returned_JSON_for_user_id(self):
        response = self.client.post('/user', data={
            'names': 'user1',
            'last_names': 'uno',
            'address': 'CRA 1 #99-88',
        })

        json_ = self.client.get(f'/user/{int(response.data)}')
        self.assertTrue(self.is_json(json_.data))

    def test_GET_returned_JSON_for_None_user_id(self):
        json_ = self.client.get(f'/user')
        self.assertTrue(self.is_json(json_.data))

    def test_GET_user_info_by_user_id(self):
        response1 = self.client.post('/user', data={
            'names': 'user1',
            'last_names': 'uno',
            'address': 'CRA 1 #99-88',
        })
        response2 = self.client.post('/user', data={
            'names': 'user2',
            'last_names': 'dos',
            'address': 'CRA 2 #99-88',
        })

        get_response1 = self.client.get(f'/user/{int(response1.data)}')
        user1_dict = json.loads(get_response1.data)
        self.assertEqual(user1_dict.get('names'), 'user1')

        get_response2 = self.client.get(f'/user/{int(response2.data)}')
        user2_dict = json.loads(get_response2.data)
        self.assertEqual(user2_dict.get('last_names'), 'dos')

    def test_GET_all_users_when_user_id_parameter_is_None(self):
        self.client.post('/user', data={
            'names': 'user1',
            'last_names': 'uno',
            'address': 'CRA 1 #99-88',
        })
        self.client.post('/user', data={
            'names': 'user2',
            'last_names': 'dos',
            'address': 'CRA 2 #99-88',
        })

        json_ = self.client.get('/user')
        users = json.loads(json_.data)
        all_users = User.query.all()
        self.assertEqual(len(users), len(all_users))
