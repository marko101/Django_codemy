from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]


#konfiguriši naslov za admina
admin.site.site_header = "Logos Administaciona strana"
admin.site.site_title = "Pretraživač"
admin.site.index_title = "Dobrodošli Admin!"