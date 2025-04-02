from ..models import PruebaDiagnostica
import manejadorEEGFile.models as EEGFile
import pyedflib

def get_pruebas_diagnosticas():
    return PruebaDiagnostica.objects.all()

def get_prueba_diagnostica(pk):
    return PruebaDiagnostica.objects.get(id=pk)

def crear_prueba_diagnostica(data):
    return PruebaDiagnostica.objects.create(**data)

def actualizar_prueba_diagnostica(pk, data):
    prueba = get_prueba_diagnostica(pk)
    for key, value in data.items():
        setattr(prueba, key, value)
    prueba.save()
    return prueba

def subir_archivo_eeg(prueba_id, archivo):
    """Sube un archivo EDF, extrae metadatos y los guarda en EEGFile."""
    prueba = get_prueba_diagnostica(prueba_id)
    
    if prueba.tipo_de_prueba != 'EEG':
        return None, "Solo las pruebas EEG pueden tener archivos EDF."

    eeg_file = EEGFile(file=archivo)

    try:
        with pyedflib.EdfReader(archivo) as f:
            eeg_file.recording_date = f.getStartdatetime()
            eeg_file.num_signals = f.signals_in_file
            eeg_file.duration = f.file_duration
            eeg_file.channel_names = f.getSignalLabels()
            eeg_file.sampling_rates = {eeg_file.channel_names[i]: f.getSampleFrequency(i) for i in range(f.signals_in_file)}

        eeg_file.save()
        prueba.eeg_file = eeg_file
        prueba.save()
        return eeg_file, None

    except Exception as e:
        return None, str(e)
