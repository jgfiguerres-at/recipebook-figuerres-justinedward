from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Profile, Ingredient, Recipe, RecipeIngredient


def recipe_list(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipebook/recipe_list.html', {
        'recipes': recipes,
    })


def recipe_detail(request, id):
    recipe = Recipe.objects.get(pk=id)
    ingredients = Ingredient.objects.filter(recipe__recipe__name=recipe.name)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    return render(request, 'recipebook/recipe_detail.html', {
        'recipe' : recipe,
        'ingredients': ingredients,
    })


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipebook/recipe_list.html' # default value


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipebook/recipe_detail.html' # default value
