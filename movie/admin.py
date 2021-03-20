from django.contrib import admin
from .models import Movie, Image, Rating, AudienceRating, Tag, Actor, Director, Genre, Type

admin.site.register(Movie)
admin.site.register(Image)
admin.site.register(Rating)
admin.site.register(AudienceRating)
admin.site.register(Tag)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Type)
