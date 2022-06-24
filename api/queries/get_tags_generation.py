from ariadne import convert_kwargs_to_snake_case
from api.check_token import token_required
import requests
from api import app
from api.models.Post import Tag
import json


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

        tag_array = []
        for tag_id in json.loads(response.text):
            tag = Tag.query.get(tag_id)
            tag_array.append(tag)

        payload = {
            "success": True,
            "tags": tag_array
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": ["Something went wrong with the AI"]
        }

    return payload
