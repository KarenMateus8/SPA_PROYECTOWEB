from app_vehiculo.models import Vehiculo
from rest_framework import serializers

class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id','modelo','marca','referencia','fecha_creacion','valor_comercial']