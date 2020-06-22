from django.shortcuts import render
from django.http import HttpResponse
from .models import tvrtke


posts=[
    {
        'naziv': 'Deloit',
        'adresa': 'dubrovačka 56, OSijek',
        'struka':' informatika',
        'datum_unosa':'28.06.2020'
    }
]


def tvrtke(request):
    
    context={
        'posts':posts
    }
    return  render(request, 'tvrtke/tvrtke.html',context)

#