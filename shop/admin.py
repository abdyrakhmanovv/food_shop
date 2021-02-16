from django.contrib import admin
from .models import Dish

# admin.site.register(dish)
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', ]
# Register your models here.
