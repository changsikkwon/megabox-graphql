import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import (
    Movie,
    Image,
    Rating,
    Actor,
    AudienceRating,
    Director,
    Genre,
    Type,
    Tag,
)


class MovieTp(DjangoObjectType):
    class Meta:
        model = Movie


class ImageTp(DjangoObjectType):
    class Meta:
        model = Image
        # filter_fields = {"type": 1}
        # interfaces = (relay.Node,)


class RatingTp(DjangoObjectType):
    class Meta:
        model = Rating


class AudienceRatingTp(DjangoObjectType):
    class Meta:
        model = AudienceRating


class TagTp(DjangoObjectType):
    class Meta:
        model = Tag


class ActorTp(DjangoObjectType):
    class Meta:
        model = Actor


class DirectorTp(DjangoObjectType):
    class Meta:
        model = Director


class GenreTp(DjangoObjectType):
    class Meta:
        model = Genre


class TypeTp(DjangoObjectType):
    class Meta:
        model = Type


class Query(ObjectType):
    all_movie = graphene.List(MovieTp)
    movie_detail = graphene.Field(MovieTp, id=graphene.ID(required=True))

    def resolve_all_movie(self, info):
        return Movie.objects.all()

    def resolve_movie_detail(self, info, id):
        return Movie.objects.get(id=id)
