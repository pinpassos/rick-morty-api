from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def characters(request):
    urlApi = requests.get('https://rickandmortyapi.com/api/character')
    content = urlApi.content

    context = {
        'content': content
    }

    return render(request, 'template', context = context)