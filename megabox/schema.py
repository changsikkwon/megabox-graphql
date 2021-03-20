import graphene
from user.query import Query as user_query
from user.mutation import Mutation as user_mutation

# from movie.query import Query as movie_query
# from reservation.query import Query as reservation_query


class Query(user_query):
    pass


class Mutation(user_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
