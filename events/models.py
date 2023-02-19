from django.db import models


class Venue(models.Model):
    ime = models.CharField("Naziv Mesta", max_length=120)
    adresa =models.CharField("Adresa Mesta", max_length=300)
    pos_broj =models.CharField("poštanski Broj", max_length=15)
    telefon = models.CharField("Kontakt Telefon", max_length=30)
    web = models.URLField("Web Adresa")
    email =models.EmailField("Email Adresa")

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
    menadzer = models.CharField(max_length=60)
    opis = models.TextField(blank=True)
    polaznici =models.ManyToManyField(Clanovi, blank=True)
 

    def __str__(self):
        return self.ime