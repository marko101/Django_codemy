from django.shortcuts import redirect, render
import calendar
from calendar import LocaleHTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Evant, Venue
#importuj korisnike iz modela iz Djanga da bi umesto vlasnik=broj video ime
from django.contrib.auth.models import User
from .forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.urls import reverse_lazy
#za generisanje PDF-a
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4


# ubaci menjenje stranica u html listi
from django.core.paginator import Paginator


# Generate a PDF File Venue List
def venue_pdf(request):
	# Create Bytestream buffer
	buf = io.BytesIO()
	# Create a canvas
	c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
	# Create a text object
	textob = c.beginText()
	textob.setTextOrigin(cm, cm)
	textob.setFont("Helvetica", 14)

	# Add some lines of text
	#lines = [
	#	"This is line 1",
	#	"This is line 2",
	#	"This is line 3",
	#]
	
	# Designate The Model
	venues = Venue.objects.all()

	# Create blank list
	lines = []

	for venue in venues:
		lines.append(venue.ime)
		lines.append(venue.adresa)
		lines.append(venue.pos_broj)
		lines.append(venue.telefon)
		lines.append(venue.web)
		lines.append(venue.email)
		lines.append(" ")

	# Loop
	for line in lines:
		textob.textLine(line)

	# Finish Up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Return something
	return FileResponse(buf, as_attachment=True, filename='venue.pdf')

def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venus.csv'

    # CSV upis
    writer = csv.writer(response)

    #razotkrivam model
    venues= Venue.objects.all()

    #dodaj kolonu csv fajlu
    writer.writerow(['Venue ime', 'Adresa', 'Poš broj', 'Telefon', 'web', 'email'])

    
    #Loop thu i izlaz
    for venue in venues:
        writer.writerow([venue.ime, venue.adresa, venue.pos_broj, venue.telefon, venue.web, venue.email])
    
    
    return response



#Generiši tekst fajl
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venus.txt'

    #razotkrivam model
    venues= Venue.objects.all()

    lines=[]
    #Loop thu i izlaz
    for venue in venues:
        lines.append(f'{venue.ime}\n{venue.adresa}')


    #lines = ["Ovo je linija 1\n",
    #         "Ovo je linija 2\n",
    #         "Ovo je linija 3\n",]
    
    #pisanje Tekstfajla
    response.writelines(lines)
    return response


# Create your views here.
def delete_venue(request, venue_id):
    venue=Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')


def delete_event(request, event_id):
    event=Evant.objects.get(pk=event_id)
    if request.user == event.menadzer:
        event.delete()
        messages.success(request, ("Događaj je obrisan!"))
        return redirect('list_events')
    else:
        messages.success(request, ("Nisi autorizovan da brišeš!"))
        return redirect('list_events')


def update_event(request, event_id):
    event = Evant.objects.get(pk=event_id)

    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list_events')
    return render(request, 'events/update_event.html', {'event':event, 'form':form})




def add_event(request):
    snimljeno = False
    if request.method == "POST":
        if request.user.is_superuser:  #user.id == 2:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Admin, Događaj je snimljen')
                return HttpResponseRedirect(reverse_lazy('list_events'))
        else:
            form = EventForm(request.POST)

            if form.is_valid():
                #form.save()
                event = form.save(commit=False) #hoću da snimim ali ne još
                event.menadzer = request.user #ovo je nakon kreiranja vlasnika u models.py
                event.save()            
                messages.success(request, 'Događaj je snimljen')
                return HttpResponseRedirect(reverse_lazy('list_events'))
    else:
        #samo idem na stranicu ništa ne snimam
        if request.user.is_superuser:
            form= EventFormAdmin
        else:
            form= EventForm
        if 'snimljeno' in request.GET:
            snimljeno = True
    return render(request, 'events/add_event.html', {'form':form, 'snimljeno':snimljeno}) # {{ form.as_p }}



def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        venue = form.save(commit=False) #hoću da snimim ali ne još
        venue.vlasnik = request.user.id #ovo je nakon kreiranja vlasnika u models.py
        venue.save()
        #form.save()
        return redirect('list-venues')
    return render(request, 'events/update_venue.html', {'venue':venue, 'form':form})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue_vlasnik = User.objects.get(pk=venue.vlasnik)
    return render(request, 'events/show_venue.html', {'venue':venue, "venue_vlasnik":venue_vlasnik})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(ime__contains=searched)
        return render(request, 'events/search_venues.html',{'searched':searched, 'venues':venues})
    else:
        return render(request, 'events/search_venues.html',
    {})


def list_venues(request):
    venue_list = Venue.objects.all().order_by('ime')

    #ubaci stranice ako je lista dugačka
    p = Paginator(Venue.objects.all(), 6)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages

    return render(request, 'events/venue.html', {'venue_list':venue_list, 'venues': venues, 'nums':nums})


def add_venue(request):
    snimljeno = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            #form.save()
            venue = form.save(commit=False) #hoću da snimim ali ne još
            venue.vlasnik = request.user.id #ovo je nakon kreiranja vlasnika u models.py
            venue.save()
            messages.success(request, 'Mesto događaja je snimljeno')
            return HttpResponseRedirect('list_venues', request)
            
    else:
        form= VenueForm
        if 'snimljeno' in request.GET:
            snimljeno = True
    return render(request, 'events/add_venue.html', {'form':form, 'snimljeno':snimljeno}) # {{ form.as_p }}


def svi_dogadjaji(request):
    event_list = Evant.objects.all().order_by('ime', 'venue') #('-datum')
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