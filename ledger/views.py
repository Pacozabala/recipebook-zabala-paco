from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe'
    
    def get_queryset(self):
        return Recipe.objects.filter(pk=self.kwargs['pk'])
    