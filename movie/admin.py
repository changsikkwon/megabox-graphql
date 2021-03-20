from django.contrib import admin
from .models import Reservation, ReservationItem, Theater, City, TheaterScreen, Screen, TicketType

admin.site.register(Reservation)
admin.site.register(ReservationItem)
admin.site.register(Theater)
admin.site.register(City)
admin.site.register(TheaterScreen)
admin.site.register(Screen)
admin.site.register(TicketType)