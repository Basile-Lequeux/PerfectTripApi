from api import db
from api.models.User import User


def create_user_resolver(obj, info, email, password, name):
    try:
        user = User(
            email=email, password=password, name=name
        )
        db.session.add(user)
        db.session.commit()
        payload = {
            "success": True,
            "user": user.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
