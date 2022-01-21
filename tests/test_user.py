import unittest

from api.models.User import User


class TestUserModel(unittest.TestCase):
    def test_encode_token(self):
        user = User(
            email="test@test.fr",
            password="test"
        )
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token) == user.id)


if __name__ == '__main__':
    unittest.main()
