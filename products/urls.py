from django.urls import path

from .views import (IngredientDetailView,
                    IngredientListView,
                    IngredientCreateView,
                    IngredientUpdateView,
                    IngredientDeleteView)


urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_details'),
    path('ingredients/create', IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredients/update/<int:pk>', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/delete/<int:pk>', IngredientDeleteView.as_view(), name='ingredient_delete'),

    # path('books/', BookListView.as_view(), name='book_list'),
    # path('books/<int:pk>/', BookDetailView.as_view(), name='book_details'),

    # path('authors/', AuthorListView.as_view(), name='author_list'),
    # path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_details')
]