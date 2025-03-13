from django.http import JsonResponse
from .models import Paciente
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_pacientes import get_pacientes, get_paciente


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    data = {"pacientes": list(pacientes.values())}
    return JsonResponse(data)

def pacientes_view(request):
    if request.method == 'GET':
        pacientes = get_pacientes()
        pacientes_dto = serializers.serialize('json', pacientes)
        return HttpResponse(pacientes_dto, content_type='application/json')

def paciente_view(request, pk):
    if request.method == 'GET':
        paciente = get_paciente(pk)
        paciente_dto = serialize('json', [paciente])  # Se serializa como JSON
        return JsonResponse(paciente_dto, safe=False)