from django import forms
from django.forms import ModelForm
from .models import Venue


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