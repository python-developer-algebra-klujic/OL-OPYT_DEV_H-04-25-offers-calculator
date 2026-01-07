from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'

    success_url = reverse_lazy('products:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

    success_url = reverse_lazy('products:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product

    success_url = reverse_lazy('products:product_list')