import json
import jwt
from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify, make_response
from http import HTTPStatus
from api.models.User import User
from api.mutations.create_post import create_post_resolver, check_valid_base64_images, build_images_urls
from api.mutations.delete_post import delete_post_resolver
from api.mutations.update_post import update_post_resolver
from api.mutations.create_user import create_user_resolver
from api.queries.get_all_tags import list_tags_resolver
from api.queries.get_destination import get_destination_resolver
from api.queries.get_user_by_token import get_user_by_token_resolver
from api.queries.get_list_posts import list_posts_resolver
from api.queries.get_post import getPost_resolver
from api.queries.login import login_resolver
from api.queries.get_list_destination import list_destination_resolver
from api.models.Post import add_tags_to_db
from api.models.Destination import add_destinations_to_db

query = ObjectType("Query")
query.set_field("listPosts", list_posts_resolver)
query.set_field("getPost", getPost_resolver)
query.set_field("login", login_resolver)
query.set_field("getUserByToken", get_user_by_token_resolver)
query.set_field("getDestination", get_destination_resolver)
query.set_field("listTags", list_tags_resolver)
query.set_field("listDestination", list_destination_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)
mutation.set_field("createUser", create_user_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = HTTPStatus.OK if success else HTTPStatus.BAD_REQUEST
    return make_response(jsonify(result), status_code)
