from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Profile, Ingredient, Recipe, RecipeIngredient


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html' # default value


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html' # default value
