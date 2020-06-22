from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class tvrtke(models.Model):
    naziv_tvrtke= models.CharField(max_length=100)
    struka=models.CharField(max_length=100)
    naziv_tvrtke_za_praksu=models.CharField(max_length=100)
    opis_zadataka=models.TextField()
    datum_objave=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv_tvrtke