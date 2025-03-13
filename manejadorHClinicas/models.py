from django.db import models


# Create your models here.

class HistorialClinico(models.Model):
    id_historial = models.AutoField(primary_key=True)
    paciente = models.OneToOneField(Historia, on_delete=models.CASCADE)
    fecha = models.DateField()
    ruta_contenido = models.TextField()

    def __str__(self):
        return f"Historial {self.id_historial}"
    

    


