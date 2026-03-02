from django.urls import path

from .views import *

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:id>', RecipeDetailView.as_view(), name='recipe_detail'),
]

app_name = "ledger"
