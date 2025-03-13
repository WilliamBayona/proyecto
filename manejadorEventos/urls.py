from django.urls import path
from .views import lista_eventos
from .views import eventos_view

urlpatterns = [
    path('eventos/', lista_eventos, name='lista_eventos'),
    path('eventos/', eventos_view, name='eventos_list'),
]
