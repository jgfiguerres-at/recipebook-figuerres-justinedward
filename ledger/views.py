from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import RecipeForm, RecipeImageForm
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


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm

    def form_valid(self, form):
        form.instance.recipe__pk = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})
