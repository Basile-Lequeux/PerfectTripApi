from api import engine
from api.check_token import token_required
from api.models.Post import Post

MIN_LENGTH_TITLE = 1


@token_required
def list_posts_resolver(obj, info, current_user, token, tags, title):
    try:
        posts_by_tags = get_posts_by_tags_count_desc(tags)
        posts = filter_by_title(posts_by_tags, title)
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


def get_posts_by_tags_count_desc(tags):
    posts = []
    if len(tags) > 0:
        tags_string = ','.join(map(str, tags))
        with engine.connect() as db_connect:
            query_string = """
                with t3 as (SELECT t1.post_id, COUNT(*) cnt FROM public.tags t1 WHERE T1.tag_id in ({}) 
                 group by 1 )
                SELECT  t2.* FROM public.post t2, t3
                WHERE   t3.post_id = t2.id
                order by t3.cnt desc;
                """.format(tags_string)

            response = db_connect.execute(query_string)
            for row in response:
                post_id = row[0]
                post = Post.query.get(post_id)
                posts.append(post.to_dict())

    else:
        posts = [post.to_dict() for post in Post.query.all()]
    return posts


def filter_by_title(posts, title):
    if len(title) >= MIN_LENGTH_TITLE:
        filtered_posts = []
        for post in posts:
            if title in post['title']:
                filtered_posts.append(post)

        return filtered_posts

    return posts


# not used
def get_posts_by_title(title):
    posts = []
    if title:
        with engine.connect() as db_connect:
            query_string = """
                SELECT *
                FROM post
                WHERE title LIKE '{}' OR  title LIKE '{}' OR title LIKE '{}'
            """.format(title + '%%', '%%' + title, '%%' + title + '%%')
            try:
                response = db_connect.execute(query_string)
                for row in response:
                    post_id = row[0]
                    post = Post.query.get(post_id)
                    posts.append(post)

            except Exception as error:
                print(error)

    return posts
