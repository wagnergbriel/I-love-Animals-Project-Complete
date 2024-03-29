from django.db import models
from pyUFbr.baseuf import ufbr
import uuid


class Colaborador(models.Model):
    """Classe que apresenta os tipos de identificação pessoal"""

    class TipoIdentificacaoPessoal(models.TextChoices):
        CPF = "CPF"
        CNPJ = "CNPJ"

    """Campos da Classe colaborador"""
    id_colaborador = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200)
    numero_celular = models.CharField(max_length=14)
    email = models.EmailField()
    senha = models.CharField(max_length=12)
    tipo_identificacao_pessoal = models.CharField(
        max_length=14, choices=TipoIdentificacaoPessoal.choices, default="CNPJ"
    )
    identificador_pessoal = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    numero_endereco = models.IntegerField()
    cep = models.CharField(max_length=8)
    estado = models.CharField(
        max_length=10, choices=[(state, state) for state in ufbr.list_uf]
    )
    cidade = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    complemento = models.CharField(max_length=500)

    def __str__(self):
        return self.nome


class Animais(models.Model):
    """Classe que apresenta os tipos de animais"""

    class TipoAnimais(models.TextChoices):
        CAT = "cat"
        DOG = "dog"

    """Campos da Classe animais"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    colaborador = models.ForeignKey("Colaborador", on_delete=models.PROTECT)
    tipo_animal = models.CharField(max_length=50, choices=TipoAnimais.choices)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_de_entrada = models.DateTimeField(auto_now_add=True)
    foto_animal = models.ImageField()
    status_de_adocao = models.BooleanField()
    raca = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
