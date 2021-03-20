from graphene_django.types import DjangoObjectType, ObjectType
from .models import Movie, Image, Rating, Actor, AudienceRating, Director, Genre, Type, Tag


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class ImageType(DjangoObjectType):
    class Meta:
        model = Image


class RatingType(DjangoObjectType):
    class Meta:
        model = Rating


class AudienceRatingType(DjangoObjectType):
    class Meta:
        model = AudienceRating


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor


class DirectorType(DjangoObjectType):
    class Meta:
        model = Director


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre


class TypeType(DjangoObjectType):
    class Meta:
        model = Type


class Query(ObjectType):
    pass
