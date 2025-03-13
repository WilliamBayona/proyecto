from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_eventos import get_eventos, get_evento, crear_evento
from django.views.decorators.csrf import csrf_exempt 
from .models import EventoMedico as Evento
from django.shortcuts import render

def lista_eventos(request):
    eventos = Evento.objects.all()
    data = {"eventos": list(eventos.values())}
    return JsonResponse(data)

@csrf_exempt
def eventos_view(request):
    if request.method == 'GET':
        evento_id = request.GET.get("evento_id", None)

        if evento_id:
            evento_dto = get_evento(evento_id)
            evento = serializers.serialize('json', [evento_dto,])
            return HttpResponse(evento, 'application/json')
        else:
            eventos_dto = get_eventos()
            eventos = serializers.serialize('json', [eventos_dto,])
            return HttpResponse(eventos, 'application/json')  

    if request.method == 'POST':
        evento_dto = crear_evento(json.loads(request.body))
        evento_json = serializers.serialize('json', [evento_dto,])
        return HttpResponse(evento, 'application/json')


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