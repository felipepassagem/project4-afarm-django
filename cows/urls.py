from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('add_owner', views.add_owner, name='add_owner'),
    path('owner_list', views.owner_list, name='owner_list'),
    path('update_owner/<int:owner_id>', views.update_owner, name='update_owner'),
    path('delete_owner/<int:owner_id>', views.delete_owner, name='delete_owner'),

    path('add_cow', views.add_cow, name = 'add_cow'),
    path('cow_list', views.cow_list, name='cow_list'),
    path('update_cow/<int:cow_id>', views.update_cow, name='update_cow'),
    path('delete_cow/<int:cow_id>', views.delete_cow, name='delete_cow'),

    path('add_farm', views.add_farm, name="add_farm"),
    path('farm_list', views.farm_list, name="farm_list"),
    path('update_farm/<int:farm_id>', views.update_farm, name="update_farm"),
    path('delete_farm/<int:farm_id>', views.delete_farm, name='delete_farm'),
]