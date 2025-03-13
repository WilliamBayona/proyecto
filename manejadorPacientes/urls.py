from django.urls import path
from .views import lista_pacientes

urlpatterns = [
    path('pacientes/', lista_pacientes, name='lista_pacientes'),
     path('pacientes/', pacientes_view, name='pacientes_list'),
]
