from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "animals_app/home.html")

def adocao():
    pass

def login(request):
    return render(request, "animals_app/login.html")