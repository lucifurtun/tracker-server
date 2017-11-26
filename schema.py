import graphene
import graphql_jwt

from apps.tracking.schema import Query as TrackingQuery
from apps.user.mutations import LogIn


class Query(TrackingQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutations(graphene.ObjectType):
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    login = LogIn.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
