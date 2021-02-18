from django.urls import path
from shop import views as v

urlpatterns = [
    path('', v.view_dishes, name='index'),
]
