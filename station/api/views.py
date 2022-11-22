from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import Station, Instructions

from .serializers import StationSerializer, InstructionsSerializer


class StationViewSet(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

    # @action(
    #     detail=True,
    #     methods=['get', 'post'],
    #     url_path='state',
    #     serializer_class=InstructionsSerializer
    # )
    # def state(self, request, pk):
    #     station = Station.objects.filter(pk=pk)
    #     print(station)
    #     if request.method == 'GET':
    #         serializer = InstructionsSerializer(station)
    #         return Response(serializer.data)
    #     else:
    #         return Response("post-post")


# class Instruction(APIView):
#     """Получение / изменение координат станции"""
#     def get(self, request, pk):
#         station = Station.objects.filter(pk=pk)
#
#     serializer_class = InstructionsSerializer
#     queryset = Instructions.objects.all()



