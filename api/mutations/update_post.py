from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models.Post import Post


@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, id, title, description):
    try:
        post = Post.query.get(id)
        if post:
            post.title = title
            post.description = description
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload