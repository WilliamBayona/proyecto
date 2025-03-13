from ..models import Evento

def get_eventos():
    eventos = Evento.objects.all()
    return eventos

def get_evento(evento_id):
    return Evento.objects.get(pk=evento_id)

def crear_evento(data):
    evento = Evento(
        historia_clinica_id=data.get("historia_clinica_id"),
        motivo=data.get("motivo"),
        fecha=data.get("fecha")
    )
    evento.save()
    return evento
