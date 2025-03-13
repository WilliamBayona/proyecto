from django.http import JsonResponse
from .models import Paciente
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_pacientes import get_pacientes


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    data = {"pacientes": list(pacientes.values())}
    return JsonResponse(data)

def pacientes_view(request):
    if request.method == 'GET':
        pacientes = get_pacientes()
        pacientes_dto = serializers.serialize('json', pacientes)
        return HttpResponse(pacientes_dto, content_type='application/json')
