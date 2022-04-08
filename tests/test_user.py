import unittest
from api.models.User import User
import app


class TestUserModel(unittest.TestCase):
    def test_decode_auth_token_should_return_user_id(self):
        user = User(
            email='test@test.com',
            password='test',
            name='John Doe'
        )
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(User.decode_auth_token(auth_token) == user.id)


if __name__ == '__main__':
    unittest.main()
