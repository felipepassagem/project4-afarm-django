from django import forms  
from django.forms import ModelForm, widgets
from .models import *

class FarmForm(ModelForm):
    class Meta:
        model =  Farm
        fields = ['farm_name','coord_lat','coord_long', 'user']

        labels = {
            'farm_name': 'Fazenda',
            'coord_lat': 'Latitude',
            'coord_long': 'Longitude',
            'user': ""
        }

        widgets = {
            'farm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'coord_lat': forms.TextInput(attrs={'class': 'form-control'}),
            'coord_long': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'hidden': 'true'})
        }
        

class CowForm(ModelForm):

    class Meta:
        model = Cow
        fields = ['ages','number','color','owner','aquisiton_date','buy_age','child_quant','last_child_birth','farm', 'vac','nota_fiscal','obs','user']

        COLORS = [('Amarelo', 'Amarelo') ,('Azul', 'Azul') ,('Branco', 'Branco') ,('Laranja', 'Laranja') ,('Preto', 'Preto'),('Rosa', 'Rosa') ,('Verde', 'Verde'), ('Vermelho', 'Vermelho')]
        BOOL_CHOICES = [('Sim', 'Sim'), ('Não', 'Não')]
        AGES = [('Bezerro', 'Bezerro'), ('Boi', 'Boi'), ('Garrote', 'Garrote'), ('Novilha', 'Novilha'), ('Vaca', 'Vaca')]

        labels = {
            'ages': 'Tipo',
            'number': "Número do brinco",
            'color': "Cor do brinco",
            'owner': "Dono",
            'aquisiton_date': "Data da compra",
            'buy_age': "Idade estimda na compra",
            'nota_fiscal': "Nota fisca em dia?",
            'child_quant': "Quantidade de bezerros paridos",
            'last_child_birth': "Data da última parida",
            'farm': 'Fazenda',
            'vac': "Vacinação em dia?",
            'obs': "Observações",
            'user': "",
        }

        widgets = {
            'ages': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'min': '0'}),
            'color': forms.Select(attrs={'class': 'form-control', }, choices=COLORS),
            'owner': forms.Select(attrs={'class': 'form-control',}),
            'aquisiton_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date',}),
            'buy_age': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'nota_fiscal': forms.Select(attrs={'class': 'form-control', }, choices=BOOL_CHOICES),
            'child_quant': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'last_child_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date',}),
            'farm': forms.Select(attrs={'class': 'form-control',}),
            'vac': forms.Select(attrs={'class': 'form-control', }, choices=BOOL_CHOICES),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'hidden': 'true'})
        }
    #def __init__(self, user=None, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    if user:
    #        test = list(user.values())
    #        print(test[13])
    #        self.fields['owner'].queryset = Owner.objects.all().filter(user=test[13])

class OwnerForm(ModelForm):

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'birth_date', 'phone', 'obs')

        lables =  {
            'first_name': 'Nome:',
            'last_name': 'Sobrenome:',
            'birth_date': 'Data de nascimento:',
            'phone': 'Telefone:',
            'obs': 'Observações:',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': 'true'}),  
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'required': 'true'},),  
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'true'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }