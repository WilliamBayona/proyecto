from ..models import Evento

def get_eventos():
    eventos = Evento.objects.all()
    return eventos
