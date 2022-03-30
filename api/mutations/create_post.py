from datetime import date

import cloudinary.uploader
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.check_token import token_required
from api.models.Destination import Destination
from api.models.Post import Post, Tag
from api.models.User import User


@token_required
@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, current_user, token, title, description, duration, budget, tags, destination, images):
    try:
        today = date.today()
        ref_destination = Destination.query.get(destination)
        images_urls = build_images_urls(images)
        post = Post(
            title=title,
            description=description,
            created_at=today.strftime("%b-%d-%Y"),
            duration=duration,
            budget=budget,
            created_by=current_user,
            destination=ref_destination,
            images_url=images_urls
        )
        for tag_id in tags:
            tag = Tag.query.get(tag_id)
            post.tags.append(tag)

        db.session.add(post)
        db.session.commit()
        posts = [post.to_dict() for post in Post.query.all()]
        payload = {
            "success": True,
            "post": post.to_dict(),
            "posts": posts
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload


def build_images_urls(images):
    image_array = []
    for image64 in images:
        #TODO check if valid image base 64
        upload_data = cloudinary.uploader.upload(image64, folder='articleImage')
        image_uri = upload_data["url"]
        image_array.append(image_uri)

    return image_array
