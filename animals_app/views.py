from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "animals_app/home.html")

def adocao():
    pass