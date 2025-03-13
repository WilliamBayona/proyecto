from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_eventos import get_eventos 
from .models import EventoMedico as Evento
from django.shortcuts import render

def lista_eventos(request):
    eventos = Evento.objects.all()
    data = {"eventos": list(eventos.values())}
    return JsonResponse(data)

def eventos_view(request):
    if request.method == 'GET':
        eventos = get_eventos()
        eventos_dto = serializers.serialize('json', eventos)
        return HttpResponse(eventos_dto, content_type='application/json')

def evento_view(request, pk):
    if request.method == 'GET':
        evento = get_evento(pk)
        evento_dto = serialize('json', [evento]) 
        return JsonResponse(evento_dto, safe=False)