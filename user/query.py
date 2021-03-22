import graphene

from graphene_django.types import DjangoObjectType, ObjectType
from .models import User, Like


class UserType(DjangoObjectType):
    class Meta:
        model = User


class LikeType(DjangoObjectType):
    class Meta:
        model = Like


class Query(ObjectType):
    all_user = graphene.List(UserType)
    
    def resolve_all_user(self, info):
        return User.objects.all()
