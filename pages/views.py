from django.views.generic import TemplateView
from django.shortcuts import render


class HomePage(TemplateView):
    template_name = 'pages/index.html'


# About us
class AboutUsPage(TemplateView):
    template_name = 'pages/about.html'


# Contact us
class ContactUsPage(TemplateView):
    template_name = 'pages/contact.html'