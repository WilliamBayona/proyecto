from ..models import HistorialClinico  # Asegúrate de que el modelo esté definido en models.py

def get_historias_clinicas():
    historias = HistorialClinico.objects.all()
    return historias
