import graphene
from user.query import Query as user_query
from user.mutation import Mutation as user_mutation
from movie.query import Query as movie_query
from movie.mutation import Mutation as movie_mutation
from reservation.query import Query as reservation_query
from reservation.mutation import Mutation as reservation_mutation


class Query(user_query, movie_query, reservation_query):
    pass


class Mutation(user_mutation, movie_mutation, reservation_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
