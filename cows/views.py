
from django.http.response import FileResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *
from .forms import CowForm, FarmForm, OwnerForm


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        user = get_object_or_404(User, pk=request.user.id)
        u_email = User.objects.filter(pk = request.user.id).values_list('email', flat=True)[0]
        
        return render(request, 'cows/cow_list.html')

def add_owner(request):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        if request.method == "GET":
            form = OwnerForm()
            return render(request, 'cows/add_owner.html', {'form': form})
        else:
            form = OwnerForm(request.POST)
            user = request.user
            print(user)
            
            f_name = request.POST['first_name']
            l_name = request.POST['last_name']
            b_date = request.POST['birth_date']
            phone = request.POST['phone']
            if request.POST['obs'] != " ":
                obs = request.POST['obs']
            else: 
                obs = ""

            Owner.objects.create(
                first_name = f_name,
                last_name = l_name,
                birth_date = b_date,
                phone = phone,
                obs = obs,
                user = user
            )
            return redirect('owner_list')

def update_owner(request, owner_id):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        owner = Owner.objects.get(pk=owner_id)
        form = OwnerForm(request.POST or None, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
        return render(request, 'cows/update_owner.html', {'owner': owner, 'form': form})

def delete_owner(request, owner_id):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        owner = Owner.objects.get(pk=owner_id)
        owner.delete()
        return redirect('owner_list')

def owner_list(request):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        user = request.user
        peoples = Owner.objects.all().filter(user = user).order_by('first_name')
        return render(request, 'cows/owner_list.html', {'peoples': peoples})

def add_cow(request):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        if request.method == "GET":
            user = request.user
            form = CowForm(initial={'user': user})
            form.fields["owner"].queryset = Owner.objects.filter(user=user)
            form.fields["farm"].queryset = Farm.objects.filter(user=user)
            
            return render(request, 'cows/add_cow.html', {'form': form, 'user': user})
        else:
            form = CowForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print('asd')
            return redirect('cow_list')

def update_cow(request, cow_id):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        cow = Cow.objects.get(pk=cow_id)
        form = CowForm(request.POST or None, instance=cow)
        if form.is_valid():
            form.save()
            return redirect('cow_list')
        return render(request, 'cows/update_cow.html', {'cow': cow, 'form': form})

def delete_cow(request, cow_id):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        cow = Cow.objects.get(pk=cow_id)
        cow.delete()
        return redirect('cow_list')

def cow_list(request):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        user = request.user
        cows = Cow.objects.all().filter(user = user).order_by('color', 'number')
        return render(request, 'cows/cow_list.html', {'cows': cows})

def add_farm(request):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        if request.method == "GET":
            user = request.user
            form = FarmForm(initial={'user': user})
            #form.fields["owner"].queryset = Owner.objects.filter(user=user)
            
            return render(request, 'cows/add_farm.html', {'form': form, 'user': user})
        else:
            form = FarmForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('farm_list')

def farm_list(request):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        user = request.user
        farms = Farm.objects.all().filter(user = user).order_by('farm_name')
        return render(request, 'cows/farm_list.html', {'farms': farms})

def update_farm(request, farm_id):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        farm = Farm.objects.get(pk=farm_id)
        form = FarmForm(request.POST or None, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('farm_list')
        return render(request, 'cows/update_farm.html', {'farm': farm, 'form': form})

def delete_farm(request, farm_id):
    if not request.user.is_authenticated:
        return render(request, 'busers/register.html')
    else:
        farm = Farm.objects.get(pk=farm_id)
        farm.delete()
        return redirect('farm_list')