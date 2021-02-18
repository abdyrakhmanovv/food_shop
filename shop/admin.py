from django.contrib import admin
from.models import Dish, Drinks

# admin.site.register(dish)
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dish_type', 'description']
# Register your models here.

@admin.register(Drinks)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dish_type', 'description']