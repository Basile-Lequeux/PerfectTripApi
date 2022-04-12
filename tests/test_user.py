import unittest
from api.models.User import User
import uuid


class TestUserModel(unittest.TestCase):
    def test_decode_auth_token_should_return_user_id(self):
        user = User(
            id=uuid.uuid4(),
            email='test@test.com',
            password='test',
            name='John Doe'
        )
        auth_token = User.encode_auth_token(str(user.id))
        payload = User.decode_auth_token(auth_token)
        self.assertTrue(payload['sub'] == str(user.id))

    def test_decode_auth_token_from_another_user_should_return_false(self):
        user1 = User(
            id=uuid.uuid4(),
            email='test@test.com',
            password='test',
            name='John Doe'
        )
        user2 = User(
            id=uuid.uuid4(),
            email='test2@test.com',
            password='test2',
            name='Lucien Bramard'
        )

        auth_token = User.encode_auth_token(str(user1.id))
        payload = User.decode_auth_token(auth_token)
        self.assertEqual(False, payload['sub'] == str(user2.id))


if __name__ == '__main__':
    unittest.main()
