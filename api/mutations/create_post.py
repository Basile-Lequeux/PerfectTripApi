import base64
from datetime import date
import cloudinary.uploader
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.check_token import token_required
from api.models.Destination import Destination
from api.models.Post import Post, Tag
from api.models.User import User
from datauri import DataURI


@token_required
@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, current_user, token, title, description, duration, budget, tags, destination,
                         images):
    try:
        today = date.today()
        try:
            ref_destination = Destination.query.get(destination)
        except:
            return {
                "success": False,
                "errors": ["Destination doesn't exists"]
            }
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
            try:
                tag = Tag.query.get(tag_id)
            except:
                return {
                    "success": False,
                    "errors": ["Tag doesn't exists"]
                }
            post.tags.append(tag)

        db.session.add(post)
        db.session.commit()
        posts = [post.to_dict() for post in Post.query.all()]
        payload = {
            "success": True,
            "post": post.to_dict(),
            "posts": posts
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload


def build_images_urls(images):
    image_array = []
    for image64 in images:
        if check_valid_base64_images(image64):
            upload_data = cloudinary.uploader.upload(image64, folder='articleImage')
            image_uri = upload_data["url"]
            image_array.append(image_uri)
    return image_array


def check_valid_base64_images(image):
    try:
        uri = DataURI(image)
        if uri.mimetype == "image/png" or uri.mimetype == "image/jpeg" and uri.is_base64:
            return True
        return False
    except Exception:
        return False
