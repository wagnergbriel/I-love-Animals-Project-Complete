from django.shortcuts import render
from django.http import HttpResponse
from .models import Colaborador, Animais
from .forms import ColaboradorForm

def home(request):
    return render(request, "animals_app/home.html")

def cadastrar_colaborador(request):
    if request.method == "POST":
        form_colaborador = ColaboradorForm(request.POST)
        if form_colaborador.is_valid():
            nome = form_colaborador.cleaned_data["nome"]
            numero_celular = form_colaborador.cleaned_data["numero_celular"]
            email = form_colaborador.cleaned_data["email"]
            senha = form_colaborador.cleaned_data["senha"]
            tipo_identificacao_pessoal = form_colaborador.cleaned_data["tipo_identificacao_pessoal"]
            identificador_pessoal = form_colaborador.cleaned_data["identificador_pessoal"]
            endereco = form_colaborador.cleaned_data["endereco"]
            numero_endereco = form_colaborador.cleaned_data["numero_endereco"]
            cep = form_colaborador.cleaned_data["cep"]
            estado = form_colaborador.cleaned_data["estado"]
            cidade = form_colaborador.cleaned_data["cidade"]
            bairro = form_colaborador.cleaned_data["bairro"]
            complemento = form_colaborador.cleaned_data["complemento"]
            
            colaborador = Colaborador.objects.create()
            colaborador.save()
    else:
        form = ColaboradorForm()
    
        return render(request, 'cadastrar.html', {'form': form})

def adocao():
    pass

def login(request):
    return render(request, "animals_app/login.html")