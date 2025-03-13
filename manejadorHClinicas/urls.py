from django.urls import path
from .views import lista_historias_clinicas

urlpatterns = [
    path('historias_clinicas/', lista_historias_clinicas, name='lista_historias_clinicas'),
    path('historias_clinicas/', historias_clinicas_view, name='historias_clinicas_list'),
]
