from django.urls import path

from .views import DashboardPage, HomePage, AboutUsPage, ContactUsPage

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('dashboard/', DashboardPage.as_view(), name='dashboard'),
    path('about/', AboutUsPage.as_view(), name='about_us'),
    path('contact/', ContactUsPage.as_view(), name='contact_us'),
]
