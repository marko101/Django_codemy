from django.contrib import admin
from .models import Venue
from .models import Clanovi
from .models import Evant

# Register your models here.
admin.site.register(Venue)
admin.site.register(Clanovi)
admin.site.register(Evant)