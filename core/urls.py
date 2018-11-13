from django.urls import path
from .views import HomePageView, ListaPageView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('lista', ListaPageView.as_view()),
]
