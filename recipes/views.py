from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render


def home(request):
    return render(request, 'global/home.html')


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')