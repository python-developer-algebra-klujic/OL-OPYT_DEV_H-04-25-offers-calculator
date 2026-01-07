from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import gettext_lazy

from .models import User


# List
class UserListView(ListView):
    model = User
    paginate_by = 10
    template_name = 'account/user_list.html'


# Create
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Email address', widget=(forms.TextInput()))
    first_name = forms.CharField(required=True, help_text='First name', widget=(forms.TextInput()))
    last_name = forms.CharField(required=True, help_text='Last name', widget=(forms.TextInput()))
    password1 = forms.CharField(required=True,
                                label=gettext_lazy('Password'),
                                help_text='Password',
                                widget=(forms.PasswordInput()))
    password2 = forms.CharField(required=True,
                                label=gettext_lazy('Password confirmation'),
                                help_text='Confirm password',
                                widget=(forms.PasswordInput()))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name',
                  'description', 'job_position', 'is_active', 'is_staff', 'is_superuser')


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'account/user_form.html'
    success_url = reverse_lazy('accounts:users')


# Update
class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(required=True, help_text='Email address', widget=(forms.TextInput()))
    first_name = forms.CharField(required=True, help_text='First name', widget=(forms.TextInput()))
    last_name = forms.CharField(required=True, help_text='Last name', widget=(forms.TextInput()))
    new_password = forms.CharField(required=True,
                                label=gettext_lazy('New Password'),
                                help_text='Password',
                                widget=(forms.PasswordInput()))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'description', 'job_position', 'is_active', 'is_staff', 'is_superuser',
                  'new_password')


class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'account/user_form.html'
    success_url = reverse_lazy('accounts:users')


# Delete
class UserDeleteView(DeleteView):
    model = User
    template_name = 'account/user_confirm_delete.html'
    success_url = reverse_lazy('accounts:users')


# Login view
class CustomLoginView(LoginView):
    template_name = 'account/login.html'


# Logout view
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('pages:index')
