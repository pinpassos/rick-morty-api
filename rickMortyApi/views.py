from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def characters(request):
    response = requests.get('https://rickandmortyapi.com/api/character')
    data = response.json()
    context = {
        'data': data["results"]
    }
    return render(request, 'rickMortyApi/index.html', context = context)