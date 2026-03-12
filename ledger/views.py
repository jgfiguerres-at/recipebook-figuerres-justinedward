from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import RecipeForm
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html' # default value


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html' # default value

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_images"] = RecipeImage.objects.all()
        return context

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
