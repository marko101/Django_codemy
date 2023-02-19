from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:godina>/<str:mesec>', views.home, name="home"),
    path('events', views.svi_dogadjaji, name='list_events'),
   
]
