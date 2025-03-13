from ..models import Evento

def get_eventos():
    eventos = Evento.objects.all()
    return eventos

def get_evento(evento_id):
    return Evento.objects.get(pk=evento_id)