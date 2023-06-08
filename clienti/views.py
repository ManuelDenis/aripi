from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'clienti/index.html'


class Echipa(TemplateView):
    template_name = 'clienti/echipa.html'
