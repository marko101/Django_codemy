from django.shortcuts import render
import calendar
from calendar import LocaleHTMLCalendar
from datetime import datetime
from .models import Evant

# Create your views here.

def svi_dogadjaji(request):
    event_list = Evant.objects.all()
    return render(request, 'events/event_list.html', {'event_list':event_list})




def home(request, godina=datetime.now().year, mesec=datetime.now().strftime('%B')):
    name = "Marko"
    mesec = mesec.capitalize()
    #konvertujem mesece iz broja u ime
    mesec_broj = list(calendar.month_name).index(mesec)
    mesec_broj = int(mesec_broj)

    #kreiraj kalendar
    cal = LocaleHTMLCalendar(firstweekday=0, locale='sr_RS.utf8').formatmonth(
        godina,
        mesec_broj)
    sad = datetime.now()
    ova_godina = sad.year
    vreme = sad.strftime('%I:%M:%S %p')
    # cal = calendar.LocaleTextCalendar(locale='sr_RS.utf8')



    return render(request,'events/home.html', {
        "ime":name,
        "godina":godina,
        "mesec":mesec,
        "mesec_broj":mesec_broj,
        "cal" : cal,
        "ova_godina":ova_godina,
        "vreme":vreme
    })