from django.urls import path

from .views import (CustomLogoutView,
                    CustomLoginView,
                    UserListView,
                    UserCreateView,
                    UserUpdateView,
                    UserDeleteView)


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),



    path('users/', UserListView.as_view(), name='users'),
    path('users/add/', UserCreateView.as_view(), name='users_add'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='users_delete')
]