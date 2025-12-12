from django.urls import path

from .views import HomePage, AboutUsPage, ContactUsPage

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('about/', AboutUsPage.as_view(), name='about_us'),
    path('contact/', ContactUsPage.as_view(), name='contact_us'),
]
