from django.views.generic import ListView, DetailView

from products.models import Ingredient


class IngredientListView(ListView):
    model = Ingredient
    context_object_name = 'ingredient_list'


class IngredientDetailView(DetailView):
    model = Ingredient
