from api import engine
from api.check_token import token_required
from api.models.Post import Post


@token_required
def list_posts_resolver(obj, info, current_user, token, tags):
    try:
        posts = []
        if len(tags) > 0:
            tags_string = ','.join(map(str, tags))
            with engine.connect() as db_connect:
                query_string = """
                        with t3 as (SELECT t1.tag_id, COUNT(*) cnt FROM public.tags t1
                        WHERE T1.tag_id in ({}) group by 1 )
                        SELECT t1.*, t2.* FROM public.tags t1, public.post t2, t3
                        WHERE  t2.id = t1.post_id and t3.tag_id = t1.tag_id
                        order by t3.cnt desc
                        """.format(tags_string)

                query = db_connect.execute(query_string)
                for row in query:
                    post = Post.query.get(row[1])
                    print(post.to_dict())
                    posts.append(post.to_dict())
        else:
            posts = [post.to_dict() for post in Post.query.all()]
        payload = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
