import json
from api.models.User import User


def login_resolver(obj, info, email, password):
    user = User.query.filter_by(email=email).first()
    if user.password == password:
        auth_token = user.encode_auth_token(str(user.id))
        payload = {
            "success": True,
            "user": user.to_dict(),
            "token": auth_token.decode()
        }
    else:
        payload = {
            "success": False,
            "error": ["Wrong email or password"]
        }

    return payload