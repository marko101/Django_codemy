from django import forms
from django.forms import ModelForm
from .models import Venue, Evant


#Kreiraj formu događaja 
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields= ('ime', 'adresa', 'pos_broj', 'telefon', 'web', 'email' )
#"__all__" # ili 

        labels = {
            'ime': '',
            'adresa':'',
            'pos_broj':'',
            'telefon':'',
            'web':'',
            'email':'',
        }

        widgets = {
            'ime': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ime mesta'}),
            'adresa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresa mesta'}),
            'pos_broj':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Poštanski broj'}),
            'telefon':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefon'}),
            'web':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web adresa'},),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Mail adresa'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = Evant
        fields= ('ime', 'event_datum', 'venue', 'menadzer', 'polaznici', 'opis' )
#"__all__" # ili 

        labels = {
            'ime': '',
            'event_datum':'',
            'venue':'Mesto događaja',
            'menadzer':'Nastavnik',
            'polaznici':'Učenici',
            'opis':'',
        }

        widgets = {
            'ime': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ime događaja'}),
            'event_datum':forms.TextInput(attrs={'class':'form-control', 'placeholder':'datum događaja'}),
            'venue':forms.Select(attrs={'class':'form-select', 'placeholder':'Mesto događaja'}),
            'menadzer':forms.Select(attrs={'class':'form-select', 'placeholder':'Vodič'}),
            'polaznici':forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Učenici'},),
            'opis':forms.Textarea(attrs={'class':'form-control', 'placeholder':'opis'}),
        }