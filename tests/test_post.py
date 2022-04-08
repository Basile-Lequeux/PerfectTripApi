from ariadne import make_executable_schema, load_schema_from_path, ObjectType, snake_case_fallback_resolvers
from graphql import graphql_sync
from unittest.mock import Mock
import unittest
import app


class TestPostModel(unittest.TestCase):
    type_defs = load_schema_from_path("schema.graphql")
    query = ObjectType("Query")
    query.set_field("listPosts", app.list_posts_resolver)
    schema = make_executable_schema(
        type_defs, query, snake_case_fallback_resolvers
    )

    def test_graphql_route_list_post(self):
        lquery = """
        query {
            listPosts{
                success
                errors
                posts{
                    title
                }
            }
        }
        """
        result = graphql_sync(self.schema, lquery)
        assert result.errors is None
