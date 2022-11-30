from .models import Station
from rest_framework import serializers


class StationSerializer(serializers.ModelSerializer):
    """Станция"""
    class Meta:
        model = Station
        fields = ('id', 'name', 'state', 'date_creation', 'date_broken')
        read_only_fields = ('state', 'date_creation', 'date_broken')


class CoordinateSerializer(serializers.ModelSerializer):
    """Координаты станции"""
    class Meta:
        model = Station
        fields = ('x', 'y', 'z')
        read_only_fields = ('x', 'y', 'z')
