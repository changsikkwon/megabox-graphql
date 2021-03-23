from django.contrib.auth import models
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import (
    IMAGE_SUB,
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

    def resolve_all_movie(self, info):
        # a = Movie.objects.filter(image=Image.objects.get(type=1))
        return Movie.objects.all()
