from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardPage(LoginRequiredMixin, TemplateView):
    template_name = 'pages/dashboard.html'


class HomePage(TemplateView):
    template_name = 'pages/index.html'


# About us
class AboutUsPage(TemplateView):
    template_name = 'pages/about.html'


# Contact us
class ContactUsPage(TemplateView):
    template_name = 'pages/contact.html'