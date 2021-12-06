from django.db import models
import pyUFbr
import uuid

class Shelter(models.Model):
    """ class which struct fields of type of personal identifier"""
    class TypePersonalIdentifier(models.TextChoices):
        cpf = 'CPF'
        cnpj = 'CNPJ'
    
    """ class which return organizacion struct of identifier"""
    class PersonalIdentifier(models.Field):
        def __init__(self, connection):
            self.connection = connection
        
        def db_type(self, connection):
            if connection == 'CPF':
                return 'char(9)'
            if connection == 'CNPJ':
                return 'char(12)'


    animals = models.ForeignKey('Animals' ,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    type_personal_identifier = models.CharField(choices=TypePersonalIdentifier.choices)
    personal_identifier = PersonalIdentifier(type_personal_identifier)
    address = models.CharField(max_length=200)
    number_address = models.IntegerField()
    cep = models.CharField(max_length=8)
    state = models.CharField(choices=pyUFbr.list_uf)
    city = models.CharField(choices=pyUFbr.list_cidades(state))
    district = models.CharField(max_length=200)
    complement = models.CharField(max_length=500)
    

    def __str__(self):
        return self.name

class Animals(models.Model):
    """ class which struct fields of type of animals"""
    class TypeAnimals(models.TextChoices):
        CAT = 'cat'
        DOG = 'dog'
    
    type_animal = models.CharField(choices=TypeAnimals.choices)
    name = models.CharField(max_length=200)
    description = models.TextField()
    intake_date = models.DateTimeField(auto_now_add=True)
    image_animal = models.ImageField(height_field=200, width_field=200)
    adoption_status = models.BooleanField()
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.name