from django.urls import path
from shop import views as v

urlpatterns = [
    path('', v.index),
    path('about/', v.about),
]
