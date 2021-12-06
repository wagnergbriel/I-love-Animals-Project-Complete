from django.db import models
from pyUFbr.baseuf import ufbr
import uuid

class Shelter(models.Model):
    """ class which struct fields of type of personal identifier"""
    class TypePersonalIdentifier(models.TextChoices):
        cpf = 'CPF'
        cnpj = 'CNPJ'
    
    """ class which return organizacion struct of identifier"""
    class PersonalIdentifierField(models.Field):
        def __init__(self, connection, *args, **kwargs):
            self.connection = connection
            super().__init__(*args, **kwargs)
        
        def db_type(self, connection):
            if self.connection == 'CPF':
                return 'char(9)'
            if self.connection == 'CNPJ':
                return 'char(12)'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animals = models.ForeignKey('Animals' ,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    type_personal_identifier = models.CharField(max_length=50, choices=TypePersonalIdentifier.choices)
    personal_identifier = PersonalIdentifierField(type_personal_identifier)
    address = models.CharField(max_length=200)
    number_address = models.IntegerField()
    cep = models.CharField(max_length=8)
    state = models.CharField(max_length=50, choices=ufbr.list_uf)
    city = models.CharField(max_length=50, choices=ufbr.list_cidades(state))
    district = models.CharField(max_length=200)
    complement = models.CharField(max_length=500)
    

    def __str__(self):
        return self.name

class Animals(models.Model):
    """ class which struct fields of type of animals"""
    class TypeAnimals(models.TextChoices):
        CAT = 'cat'
        DOG = 'dog'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_animal = models.CharField(max_length=50, choices=TypeAnimals.choices)
    name = models.CharField(max_length=200)
    description = models.TextField()
    intake_date = models.DateTimeField(auto_now_add=True)
    image_animal = models.ImageField(height_field=200, width_field=200)
    adoption_status = models.BooleanField()
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.name