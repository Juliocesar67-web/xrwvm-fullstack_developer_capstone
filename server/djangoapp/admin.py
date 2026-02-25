from django.contrib import admin

from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "car_make", "type", "year")


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


# CarMakeAdmin class with CarModelInline

# Register models here
