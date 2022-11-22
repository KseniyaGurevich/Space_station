from .models import Station, Instructions
from rest_framework import serializers


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'name', 'state', 'date_creation', 'date_broken')
        read_only_fields = ('state', 'date_creation', 'date_broken')


class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = ('id', 'user', 'axis', 'distance')
        read_only_fields = ('user', 'distance')
