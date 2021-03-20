from graphene_django.types import DjangoObjectType, ObjectType
from .models import Theater, City, TheaterScreen, TicketType, Screen, Reservation, ReservationItem


class TheaterType(DjangoObjectType):
    class Meta:
        model = Theater


class CityType(DjangoObjectType):
    class Meta:
        model = City


class TheaterScreenType(DjangoObjectType):
    class Meta:
        model = TheaterScreen


class ScreenType(DjangoObjectType):
    class Meta:
        model = Screen


class ReservationType(DjangoObjectType):
    class Meta:
        model = Reservation


class ReservationItemType(DjangoObjectType):
    class Meta:
        model = ReservationItem


class TicketTypeType(DjangoObjectType):
    class Meta:
        model = TicketType


class Query(ObjectType):
    pass
