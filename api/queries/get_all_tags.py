from api.models.Post import Tag


def list_tags_resolver(obj, info):
    try:
        tags = [post.to_dict() for post in Tag.query.all()]
        payload = {
            "success": True,
            "posts": tags
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload