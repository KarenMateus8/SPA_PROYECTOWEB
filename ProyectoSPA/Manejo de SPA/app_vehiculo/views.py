from app_vehiculo.models import Vehiculo
from rest_framework import viewsets
from rest_framework.response import Response
from app_vehiculo.serializadores import VehiculoSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Event
# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by('-fecha_creacion')
    serializer_class = VehiculoSerializer


def get_events(request):
    events = Event.objects.all()
    events_list = [{"id": event.id, "title": event.title, "start": event.start.isoformat()} for event in events]
    return JsonResponse(events_list, safe=False)

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Event.objects.create(title=data['title'], start=data['start'])
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)

@csrf_exempt
def edit_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            event = Event.objects.get(id=data['id'])
            event.title = data['title']
            event.save()
            return JsonResponse({"success": True})
        except Event.DoesNotExist:
            return JsonResponse({"success": False, "error": "Evento no encontrado"}, status=404)
    return JsonResponse({"success": False}, status=400)

@csrf_exempt
def delete_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            event = Event.objects.get(id=data['id'])
            event.delete()
            return JsonResponse({"success": True})
        except Event.DoesNotExist:
            return JsonResponse({"success": False, "error": "Evento no encontrado"}, status=404)
    return JsonResponse({"success": False}, status=400)