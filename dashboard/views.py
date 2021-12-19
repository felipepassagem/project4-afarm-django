from cows.models import *
from django.shortcuts import render
from collections import Counter, OrderedDict
from django.http import HttpResponse
from collections import OrderedDict
from datetime import datetime, timedelta, date

from .fusioncharts import FusionCharts
# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        user = request.user
        #
        n_animals = Cow.objects.all().filter(user = user).count()
        n_cows = Cow.objects.all().filter(user = user, ages="Vaca").count()
        n_bez = Cow.objects.all().filter(user = user, ages="Bezerro").count()
        n_bull = Cow.objects.all().filter(user = user, ages="Boi").count()
        #

        ##
        cowtype_pie_chart = get_animal_type(user)[0]
        cowtype_column_chart = get_animal_type(user)[1]
        ##

        ###
        animal_per_owner_list = []
        owners = list(Owner.objects.all().filter(user = user))
        owners_name_str = []
        
        for owner in owners:
            total_animals_owner = Cow.objects.all().filter(owner = owner).count()
            animal_per_owner_list.append(total_animals_owner)
            owners_name_str.append(owner.first_name + " " + owner.last_name)
        ###
    
        owner_animal_chart_col = get_animals_per_owner_chats(user)[0]
        owner_animal_chart_pie = get_animals_per_owner_chats(user)[1]
        
        context = {
            'owner_animal_chart_col': owner_animal_chart_col.render(),
            'owner_animal_chart_pie': owner_animal_chart_pie.render(),
            'cowtype_column_chart': cowtype_column_chart.render(),
            'cowtype_pie_chart': cowtype_pie_chart.render(),
            'n_animals': n_animals,
            'n_cows': n_cows,
            'n_bez': n_bez,
            'n_bull': n_bull,
            'user': user,
            
        }
    return render(request, 'dashboard/dashboard.html', context)

###
def get_cowtype_dict_sorted(cows):
    cow_type_list = []
    for cow in cows:
        cow_type_list.append(cow.ages)
        
        cow_type_dict = dict(Counter(cow_type_list))
        cow_type_dict_sorted = sorted(cow_type_dict.items(), key=lambda x: x[1], reverse=True)

    return cow_type_dict_sorted

def get_animal_type(user):
    
    cows = Cow.objects.all().filter(user = user)
    cowtype_dict_sorted = get_cowtype_dict_sorted(cows)
    
    dataSource0 = OrderedDict()
    chartConfig0 = OrderedDict()
    chartConfig0 = OrderedDict()
    chartConfig0["palettecolors"] = "3C7EDD, 1FD826,E7E422,E74C22,CC4ADE,EAA829,56DFF1,E463CD"
    chartConfig0["caption"] = "Tipo de Animal"
    chartConfig0["subCaption"] = ""
    chartConfig0["xAxisName"] = "Tipo"
    chartConfig0["yAxisName"] = "Quantidade"
    chartConfig0["numberSuffix"] = ""
    chartConfig0["theme"] = "fusion"
    
    dataSource0["data"] = []
    for k, v in cowtype_dict_sorted:
        
        dataSource0['data'].append({"label":'{}'.format(k), "value": '{}'.format(v)} )    
        

    dataSource0["chart"] = chartConfig0

    cowtype_chart_pie = FusionCharts("pie2d", "cowtype_pie_chart", "100%", "350", "cowtype_pie_chart-container", "json", dataSource0)
    cowtype_chart_col = FusionCharts("column2d", "cowtype_column_chart", "100%", "350", "cowtype_column_chart-container", "json", dataSource0)
    return cowtype_chart_pie, cowtype_chart_col
###

#$$$#
def get_animals_per_owner_chats(user):
    animal_per_owner_list = []
    owners = list(Owner.objects.all().filter(user = user))
    owners_name_str = []
    
    for owner in owners:
        
        total_animals_owner = Cow.objects.all().filter(owner = owner).count()
        animal_per_owner_list.append(total_animals_owner)
        owners_name_str.append(owner.first_name + " " + owner.last_name)
    owner_animal_dict = tuple(zip(owners_name_str, animal_per_owner_list ))

    dataSource0 = OrderedDict()
    chartConfig0 = OrderedDict()
    chartConfig0 = OrderedDict()
    chartConfig0["palettecolors"] = "3C7EDD, 1FD826,E7E422,E74C22,CC4ADE,EAA829,56DFF1,E463CD"
    chartConfig0["caption"] = "Animais/Pessoa"
    chartConfig0["subCaption"] = ""
    chartConfig0["xAxisName"] = "Pessoa"
    chartConfig0["yAxisName"] = "Quantidade"
    chartConfig0["numberSuffix"] = ""
    chartConfig0["theme"] = "fusion"

    dataSource0["data"] = []
    for k, v in owner_animal_dict:
        
        dataSource0['data'].append({"label":'{}'.format(k), "value": '{}'.format(v)} )    
        

    dataSource0["chart"] = chartConfig0

    owner_animal_chart_pie = FusionCharts("pie2d", "owner_animal_chart_pie", "100%", "350", "owner_animal_chart_pie-container", "json", dataSource0)
    owner_animal_chart_col = FusionCharts("column2d", "owner_animal_chart_col", "100%", "350", "owner_animal_chart_col-container", "json", dataSource0)
    return owner_animal_chart_col, owner_animal_chart_pie