from ariadne import convert_kwargs_to_snake_case
from api import db
from api.check_token import token_required
from api.models.Post import Post, Tag


@token_required
@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, current_user, token, id, tags):
    try:
        post = Post.query.get(id)
        if post:
            array_tags = []
            for tag_id in tags:
                tag = Tag.query.get(tag_id)
                if tag:
                    array_tags.append(tag)

            post.tags = array_tags
            db.session.add(post)
            db.session.commit()
            posts = [post.to_dict() for post in Post.query.all()]
            payload = {
                "success": True,
                "post": post.to_dict(),
                "posts": posts
            }
        else:
            payload = {
                "success": False,
                "errors": ["item matching id {id} not found"]
            }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["an error occured"]
        }
    return payload
