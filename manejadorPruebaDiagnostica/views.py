from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import pyedflib
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PruebaDiagnostica, EEGFile
from .logic.logic_PruebaDiagnostica import (
    get_pruebas_diagnosticas, 
    get_prueba_diagnostica, 
    crear_prueba_diagnostica, 
    actualizar_prueba_diagnostica,
    subir_archivo_eeg
)
import json

def lista_pruebas_diagnosticas(request):
    pruebas = get_pruebas_diagnosticas()
    data = {"pruebas_diagnosticas": list(pruebas.values())}
    return JsonResponse(data)

@csrf_exempt
def pruebas_diagnosticas_view(request):
    if request.method == 'GET':
        prueba_id = request.GET.get("prueba_id", None)

        if prueba_id:
            prueba_dto = get_prueba_diagnostica(prueba_id)
            prueba = serializers.serialize('json', [prueba_dto])
            return HttpResponse(prueba, content_type='application/json')
        else:
            pruebas_dto = get_pruebas_diagnosticas()
            pruebas = serializers.serialize('json', pruebas_dto)
            return HttpResponse(pruebas, content_type='application/json')

    if request.method == 'POST':
        prueba_dto = crear_prueba_diagnostica(json.loads(request.body))
        prueba_json = serializers.serialize('json', [prueba_dto])
        return HttpResponse(prueba_json, content_type='application/json')

@csrf_exempt
def prueba_diagnostica_view(request, pk):
    if request.method == 'GET':
        prueba = get_prueba_diagnostica(pk)
        prueba_dto = serializers.serialize('json', [prueba])
        return JsonResponse(prueba_dto, safe=False)

    if request.method == 'PUT':
        prueba_dto = actualizar_prueba_diagnostica(pk, json.loads(request.body))
        prueba = serializers.serialize('json', [prueba_dto])
        return HttpResponse(prueba, content_type='application/json')

@csrf_exempt
def subir_eeg_view(request, pk):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({"error": "No se envió ningún archivo."}, status=400)

        archivo = request.FILES['file']
        eeg_file, error = subir_archivo_eeg(pk, archivo)

        if error:
            return JsonResponse({"error": error}, status=400)

        eeg_json = serializers.serialize('json', [eeg_file])
        return HttpResponse(eeg_json, content_type='application/json')
    

@api_view(['POST'])
def upload_eeg(request, prueba_id):
    """Sube un archivo EDF y lo asocia a una PruebaDiagnostica de tipo EEG."""
    try:
        prueba = PruebaDiagnostica.objects.get(id=prueba_id)

        if prueba.tipo_de_prueba != 'EEG':
            return Response({"error": "Solo las pruebas EEG pueden tener archivos EDF."}, status=400)

        if 'file' not in request.FILES:
            return Response({"error": "No se envió ningún archivo."}, status=400)

        file = request.FILES['file']
        eeg_file = EEGFile(file=file)

        # Extraer metadatos usando pyedflib
        with pyedflib.EdfReader(file) as f:
            eeg_file.recording_date = f.getStartdatetime()
            eeg_file.num_signals = f.signals_in_file
            eeg_file.duration = f.file_duration
            eeg_file.channel_names = f.getSignalLabels()
            eeg_file.sampling_rates = {eeg_file.channel_names[i]: f.getSampleFrequency(i) for i in range(f.signals_in_file)}

        eeg_file.save()

        # Asociar el archivo EDF con la prueba diagnóstica
        prueba.eeg_file = eeg_file
        prueba.save()

        return Response({"message": "Archivo EEG guardado correctamente."})
    
    except PruebaDiagnostica.DoesNotExist:
        return Response({"error": "Prueba diagnóstica no encontrada."}, status=404)
