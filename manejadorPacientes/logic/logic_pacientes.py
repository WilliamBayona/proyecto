from ..models import Paciente  # Asegúrate de que el modelo esté definido en models.py

def get_pacientes():
    pacientes = Paciente.objects.all()
    return pacientes
