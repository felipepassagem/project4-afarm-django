from django.db import models
from django.db.models.fields import CharField, DateTimeField, DateField
import datetime
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils import timezone


class Owner(models.Model):
    first_name = models.CharField(max_length=50, null = False)
    last_name = models.CharField(max_length=50, blank= True, null = True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    obs = models.TextField(max_length = 1000, blank = True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Farm(models.Model):
    farm_name = models.CharField(max_length=50, blank=True, null=False)
    coord_lat = models.CharField(max_length=50, blank=True, null=True)
    coord_long = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.farm_name)

class Cow(models.Model):
    today = datetime.date.today()
    date = today.strftime("%d/%m/%y")
    COLORS = [('Amarelo', 'Amarelo') ,('Azul', 'Azul') ,('Branco', 'Branco') ,('Laranja', 'Laranja') ,('Preto', 'Preto'),('Rosa', 'Rosa') ,('Verde', 'Verde'), ('Vermelho', 'Vermelho')]
    BOOL_CHOICES = [('Sim', 'Sim'), ('Não', 'Não')]
    AGES = [('Bezerro', 'Bezerro'), ('Boi', 'Boi'), ('Garrote', 'Garrote'), ('Novilha', 'Novilha'), ('Vaca', 'Vaca')]

    ages = models.CharField(default="Vaca", choices=AGES, max_length=50)
    number = models.IntegerField(default=000, blank = False)
    color = models.CharField(default="Azul", choices=COLORS, max_length=50)
    owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)
    aquisiton_date = models.DateField(auto_now=False, blank=True, null=True, default=date)
    buy_age= models.IntegerField(default=1, blank= True, null = True)
    child_quant = models.IntegerField(default=0, blank = True, null=True)
    last_child_birth = models.DateField(auto_now=False, blank=True, default=date, null=True)
    farm = models.ForeignKey(Farm, null=True, blank=True, on_delete=models.SET_NULL)
    vac = models.CharField(max_length=50, blank=True, null=True, choices=BOOL_CHOICES)
    nota_fiscal = models.CharField(max_length=50, blank=True, null=True, choices=BOOL_CHOICES)
    obs = models.TextField(blank=True, max_length=1000)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return str(self.number)

