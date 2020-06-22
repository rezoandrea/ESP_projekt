from django.shortcuts import render
from django.http import HttpResponse


def studenti(request):
    
    return  render(request, 'studenti/student.html')




