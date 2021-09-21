from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def characters(request):
    urlApi = requests.get('https://rickandmortyapi.com/api/character')
    context = {
        
    }
    return render(request, 'template', context = context)