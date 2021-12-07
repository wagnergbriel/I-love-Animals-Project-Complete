from django.db import models
from pyUFbr.baseuf import ufbr
import uuid

class Shelter(models.Model):
    """class which struct fields of type of personal identifier"""
    class TypePersonalIdentifier(models.TextChoices):
        CPF = 'CPF'
        CNPJ = 'CNPJ'
    
    """Fields of class Shelter"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animals = models.ForeignKey('Animals' ,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    type_personal_identifier = models.CharField(max_length=10, choices=TypePersonalIdentifier.choices, default="CNPJ")
    personal_identifier = models.CharField(max_length=14)
    address = models.CharField(max_length=200)
    number_address = models.IntegerField()
    cep = models.CharField(max_length=8)
    state = models.CharField(max_length=10, choices=[(state, state) for state in ufbr.list_uf])
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    complement = models.CharField(max_length=500)
   
    def __str__(self):
        return self.name

class Animals(models.Model):
    """ class which struct fields of type of animals"""
    class TypeAnimals(models.TextChoices):
        CAT = 'cat'
        DOG = 'dog'
    
    """Fields of class Animal"""
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