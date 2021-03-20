import graphene
from user.schema import Query as user_query, Mutation as user_mutation
from movie.schema import Query as movie_query, Mutation as movie_mutation
from reservation.schema import Query as reservation_query, Mutation as reservation_mutation


class Query(user_query, movie_query):
    pass


class Mutation(user_mutation, movie_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)