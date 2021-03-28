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
    main_image = graphene.String()

    class Meta:
        model = Movie

    def resolve_main_image(self, info):
        if Image.objects.filter(type=1, movie_id=self.id):
            image = Image.objects.get(type=1, movie_id=self.id).url
        else:
            image = None
        return image


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
    movie_detail = graphene.Field(MovieTp, id=graphene.ID(required=True))

    def resolve_all_movie(self, info):
        return Movie.objects.all()

    def resolve_movie_detail(self, info, id):
        return Movie.objects.get(id=id)
