from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_historiasClinicas import get_historias_clinicas  
from .models import HistorialClinico

def lista_historias_clinicas(request):
    historias = HistorialClinico.objects.all()
    data = {"historias_clinicas": list(historias.values())}
    return JsonResponse(data)

def historias_clinicas_view(request):
    if request.method == 'GET':
        historias = get_historias_clinicas()
        historias_dto = serializers.serialize('json', historias)
        return HttpResponse(historias_dto, content_type='application/json')
