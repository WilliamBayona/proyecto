from django.db import models
from manejadorPacientes.models import Paciente


# Create your models here.

class HistorialClinico(models.Model):
    id_historial = models.AutoField(primary_key=True)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    ruta_contenido = models.TextField()

    def __str__(self):
        return f"Historial de {self.id_historial} - {self.paciente.nombre}"
    

    


