from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from products.models import Ingredient


class IngredientListView(ListView):
    model = Ingredient
    context_object_name = 'ingredients'


class IngredientDetailView(DetailView):
    model = Ingredient


class IngredientCreateView(CreateView):
    model = Ingredient
    fields = '__all__'

    success_url = reverse_lazy('products:ingredient_list')
