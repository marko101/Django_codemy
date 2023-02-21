from django.shortcuts import render
import calendar
from calendar import LocaleHTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Evant, Venue
from .forms import VenueForm

# Create your views here.
def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/prikaz_dogadjaja.html', {'venue':venue})



def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/mesto_dogadjaja.html', {'venue_list':venue_list})


def add_venue(request):
    snimljeno = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?snimljeno=True')
    else:
        form= VenueForm
        if 'snimljeno' in request.GET:
            snimljeno = True
    return render(request, 'events/add_venue.html', {'form':form, 'snimljeno':snimljeno}) # {{ form.as_p }}


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