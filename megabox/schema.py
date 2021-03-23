import graphene
import graphql_jwt

from user.query import Query as user_query
from user.mutation import Mutation as user_mutation
from movie.query import Query as movie_query

# from reservation.query import Query as reservation_query


class Query(user_query, movie_query):
    pass


class Mutation(user_mutation):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
