from api.check_token import token_required
from api.models.User import User


@token_required
def get_user_by_token_resolver(obj, info, current_user, token):
    payload = {
        "success": True,
        "user": current_user.to_dict(),
        "token": token
    }

    return payload
