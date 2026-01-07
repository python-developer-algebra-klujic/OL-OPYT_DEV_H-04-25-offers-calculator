from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Ingredient


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    context_object_name = 'ingredients'


class IngredientDetailView(DetailView):
    model = Ingredient


class IngredientCreateView(CreateView):
    model = Ingredient
    fields = '__all__'

    success_url = reverse_lazy('products:ingredient_list')


class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = '__all__'
    template_name_suffix = '_update_form'

    success_url = reverse_lazy('products:ingredient_list')


class IngredientDeleteView(DeleteView):
    model = Ingredient

    success_url = reverse_lazy('products:ingredient_list')