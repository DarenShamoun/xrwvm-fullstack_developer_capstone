from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Allows adding one more CarModel entry at a time


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year']
    search_fields = ['name']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Displays CarModelInline within CarMake admin page
    list_display = ['name', 'description']
    search_fields = ['name']


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
