from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.check_token import token_required
from api.models.Post import Post, Tag
from api.models.User import User


@token_required
@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, current_user, token, title, description, tags):
    try:
        today = date.today()
        post = Post(
            title=title,
            description=description,
            created_at=today.strftime("%b-%d-%Y"),
            created_by=current_user
        )
        for tag_id in tags:
            tag = Tag.query.get(tag_id)
            post.tags.append(tag)

        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload
