from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models.Post import Post, Tag


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description, tags):
    try:
        today = date.today()
        post = Post(
            title=title, description=description, created_at=today.strftime("%b-%d-%Y")
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