from ..models import Paciente  # Asegúrate de que el modelo esté definido en models.py

def get_pacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def get_paciente(paciente_id):
    return Paciente.objects.get(pk=paciente_id)

def crear_paciente(data):
    paciente = Paciente(
        paciente_id=data.get("paciente_id"),
        nombre=data.get("nombre"),
        id_historial=data.get("id_historial"),
        edad=data.get("edad"),
        genero=data.get("genero"),
        tipo_sangre=data.get("tipo_sangre"),
        alergias=data.get("alergias"),
        condiciones_medicas=data.get("condiciones_medicas")
    )
    paciente.save()
    return paciente
