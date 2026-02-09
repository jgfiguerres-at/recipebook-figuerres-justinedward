from django.urls import path

from .views import *

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/<int:number>', recipe, name='recipe'),
]

app_name = "ledger"