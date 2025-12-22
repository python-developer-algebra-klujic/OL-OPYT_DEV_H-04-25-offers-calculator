from django.urls import path

from .views import (IngredientDetailView,
                    IngredientListView,
                    IngredientCreateView,
                    IngredientUpdateView,
                    IngredientDeleteView,

                    ProductDetailView,
                    ProductListView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteView)


urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_details'),
    path('ingredients/create', IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredients/update/<int:pk>', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/delete/<int:pk>', IngredientDeleteView.as_view(), name='ingredient_delete'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]