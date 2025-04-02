from django.db import models
import manejadorEEGFile.models as EEGFile
from manejadorTipoExamen.models import TipoExamen

class PruebaDiagnostica(models.Model):
    tipo_de_prueba = models.CharField(
        max_length=10,
        choices=TipoExamen.choices,
        default=TipoExamen.PRUEBA_EEG
    )
    fecha = models.DateTimeField()
    resultados = models.TextField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    presencia_anomalia = models.BooleanField(default=False)
    tipo_anomalia = models.CharField(max_length=255, null=True, blank=True)
    presencia_lesion = models.BooleanField(default=False)
    tipo_lesion = models.CharField(max_length=255, null=True, blank=True)
    presencia_sobreexpresion = models.BooleanField(default=False)
    
    eeg_file = models.OneToOneField('manejadorEEGFile.EEGFile', on_delete=models.CASCADE, null=True, blank=True)
    historial_clinico = models.ForeignKey('manejadorHClinicas.HistorialClinico', on_delete=models.CASCADE)
    paciente = models.ManyToManyField('manejadorPacientes.Paciente')
    def __str__(self):
        return f"{self.get_tipo_de_prueba_display()} - {self.fecha}"