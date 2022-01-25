from api.check_token import token_required
from api.models.Post import Post
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
@token_required
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload
