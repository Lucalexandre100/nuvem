from django.urls import path

from .views import *

urlpatterns = [
    path(
        '',
        HomePageView.as_view(),
        name='home',
    ),
    path(
        'lista',
        ListaPageView.as_view(),
        name='lista'
    ),

    # ARQUIVOS
    path(
        'arquivo-list',
        ArquivoListView.as_view(),
        name='arquivo-list',
    ),
    path(
        'arquivo-detail/<int:pk>',
        ArquivoDetailView.as_view(),
        name='arquivo-detail',
    ),
    path(
        'arquivo-update/<int:pk>',
        ArquivoUpdateView.as_view(),
        name='arquivo-update',
    ),
    path(
        'arquivo-delete/<int:pk>',
        ArquivoDeleteView.as_view(),
        name='arquivo-delete',
    ),
    path(
        'arquivo-create',
        ArquivoCreateView.as_view(),
        name='arquivo-create',
    ),

]
