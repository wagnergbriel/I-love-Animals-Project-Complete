from django.urls import path
from animals_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("adocao/", views.adocao, name="adocao"),
    path("login/", views.login, name="login"),
    path("cadastrar_colaborador/", views.cadastrar_colaborador, name="cadastrar_colaborador")
]