from ariadne import convert_kwargs_to_snake_case
from api.check_token import token_required
import requests
from api import app


@token_required
@convert_kwargs_to_snake_case
def get_tags_generation_resolver(obj, info, current_user, token, images_array):
    try:
        url = app.config.get('PERFECT_TRIP_AI_URL')
        params_array = []
        for image in images_array:
            json_object = {"img": image}
            params_array.append(json_object)
        params = {"img_data": params_array}
        response = requests.post(url, json=params)
        print(response.text)

        payload = response.text
    except ValueError:
        payload = {
            "success": False,
            "errors": "Something went wrong"
        }

    return payload
