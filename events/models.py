from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    ime = models.CharField("Naziv Mesta", max_length=120)
    adresa =models.CharField("Adresa Mesta", max_length=300)
    pos_broj =models.CharField("poštanski Broj", max_length=15)
    telefon = models.CharField("Kontakt Telefon", max_length=30, blank=True)
    web = models.URLField("Web Adresa", blank=True)
    email =models.EmailField("Email Adresa", blank=True)
    vlasnik= models.IntegerField("Vlasnik događaja", blank=False, default=1)


    def __str__(self):
        return self.ime
    
class Clanovi(models.Model):
    ime =models.CharField("Ime", max_length=30)
    prezime =models.CharField("Prezime", max_length=30)
    telefon =models.CharField("Kontakt Telefon", max_length=30)
    email =models.EmailField("Email Adresa")

    def __str__(self):
        return self.ime + ' ' + self.prezime 

class Evant(models.Model):
    ime = models.CharField("Ime Dogadjaja", max_length=120)
    event_datum = models.DateTimeField("Dan Dogadjaja")
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #mesto_dogadjaja = models.CharField("Mesto Dogadjaja", max_length=120)
    menadzer = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    opis = models.TextField(blank=True)
    polaznici =models.ManyToManyField(Clanovi, blank=True)
 

    def __str__(self):
        return self.ime