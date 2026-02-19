from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Ingredient, Recipe, RecipeIngredient


def recipe_list(request):
    recipes = Recipe.objects.all()

    return render(request, "recipebook/recipe_list.html", {
        "recipes": recipes
    })


def recipe_detail(request, id):
    recipe = recipe.objects.get(pk=id)

    return render(request, "recipebook/recipe.html", {
        "ingredients": ingredients
    })

class RecipeListView(ListView):
    model = Recipe
    template_name = 'blogpage/recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'blogpage/recipe.html'
