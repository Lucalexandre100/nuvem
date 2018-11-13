from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proj'] = 'Projeto Python'
        return context

class ListaPageView(TemplateView):
    template_name = 'lista.html'