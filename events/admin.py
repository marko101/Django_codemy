from django.contrib import admin
from .models import Venue
from .models import Clanovi
from .models import Evant

# Register your models here.
#admin.site.register(Venue, VenueAdmin) ovaj red je jednak redu @admin.register
admin.site.register(Clanovi)
#admin.site.register(Evant)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('ime', 'adresa', 'telefon')
    ordering = ('ime',)
    search_fields = ('ime', 'adresa')


@admin.register(Evant)
class EventAdmin(admin.ModelAdmin):
    fields = (('ime', 'venue'), 'event_datum', 'opis', 'menadzer', 'polaznici')
    list_display=('ime', 'event_datum', 'venue')
    list_filter=('event_datum', 'venue')
    ordering = ('-event_datum',)