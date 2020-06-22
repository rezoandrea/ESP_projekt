from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class studenti(models.Model):
    ime_studenti = models.CharField(max_length=100)
    OIB = models.CharField(max_length=100)
    fakultet = models.CharField(max_length=100)
    razdoblje_prakse = models.DateField ((""), auto_now=False, auto_now_add=False)
    opis_zadataka = models.TextField()
    ocjena = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class tvrtke(models.Model):
    studenti = models.ForeignKey(User, on_delete = models.CASCADE)
    naziv_tvrtke = models.CharField(max_length=100)
    djelatnost = models.CharField(max_Length=100)
    mjesto = models.CharField(max_length=100)
    
