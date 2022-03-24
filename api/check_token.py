from functools import wraps
import jwt
from flask import jsonify, make_response
from api import app
from api.models.User import User


def token_required(func):
    @wraps(func)
    def wrapper(obj, info, *args, **kwargs):
        token = None
        user_id = None
        payload = None

        request = info.context
        if request.headers.get('authorization'):
            token = request.headers.get("authorization").split()[1]  # delete string 'Bearer'

        if not token:
            payload = {
                "success": False,
                "errors": ["need token"],
            }

        try:
            payload = jwt.decode(token, app.config.get('SECRET_KEY'))
            user_id = payload['sub']
        except jwt.ExpiredSignatureError:
            payload = {
                "success": False,
                "errors": ["Signature expired. Please log in again."],
            }
        except jwt.InvalidTokenError:
            payload = {
                "success": False,
                "errors": ["Invalid token. Please log in again."],
            }

        current_user = User.query.get(user_id)

        if current_user:
            return func(obj, info, current_user, token, *args, **kwargs)
        else:
            return payload

    return wrapper
