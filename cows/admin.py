from django.contrib import admin

from .models import *


# Register your models here.
class DisplayCow(admin.ModelAdmin):
    list_display = ('id', 'number', 'color', 'owner')
    list_display_links = ('id', 'number', 'color', 'owner')
    search_fields = ('id', 'number', 'color', 'owner')
    list_per_page = (10)

class DisplayOwner(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone')
    list_display_links = ('id', 'first_name', 'phone')
    search_fields = ('id', 'first_name', 'phone')
    list_per_page = (10)

class DisplayFarm(admin.ModelAdmin):
    list_display = ('id', 'farm_name')
    list_display_links = ('id', 'farm_name')
    search_fields = ('id', 'farm_name')
    list_per_page = (10)



admin.site.register(Cow, DisplayCow)
admin.site.register(Owner, DisplayOwner)
admin.site.register(Farm, DisplayFarm)
