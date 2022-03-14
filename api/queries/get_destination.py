from api.check_token import token_required
from api.models.Destination import Destination
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
@token_required
def get_destination_resolver(obj, info, current_user, token, id):
    try:
        destination = Destination.query.get(id)
        print(destination.to_dict())
        payload = {
            "success": True,
            "destination": destination.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload
#desti = Destination.query.filter(Destination.tags.any(id=1))