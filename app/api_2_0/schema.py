import graphene
from graphene import relay
from flask_graphql import GraphQLView
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from .. import db
from . import api_v2
from ..models import Post


class Post(SQLAlchemyObjectType):

    class Meta:
        model = Post
        interfaces = (relay.Node,)



class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(Post)


schema = graphene.Schema(query=Query, types=[Post])
api_v2.add_url_rule('/posts', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
