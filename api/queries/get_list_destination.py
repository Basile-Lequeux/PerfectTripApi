from api.models.Destination import Destination


def list_destination_resolver(obj, info):
    try:
        destinations = [destination.to_dict() for destination in Destination.query.all()]
        payload = {
            "success": True,
            "destinations": destinations
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
