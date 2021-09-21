from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def characters(request):
    return HttpResponse('This is our main page of Rick and Morty Application.')