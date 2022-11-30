from django.utils import timezone
from drf_spectacular.utils import extend_schema
import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Station, Instructions

from .serializers import StationSerializer, CoordinateSerializer


class StationViewSet(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

    @extend_schema(
        description='Список станций',
        request=StationSerializer,
        responses={200: StationSerializer},
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        description='Создать станцию.',
        request=StationSerializer,
        responses=StationSerializer,
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(description='Получение координат станции.',
                   methods=["GET"],
                   responses={200: CoordinateSerializer},
                   )
    @extend_schema(description='Изменение позиции станции.',
                   methods=["POST"],
                   responses={201: CoordinateSerializer},
                   )
    @action(
        detail=True,
        methods=['GET', 'POST'],
        url_path='state',
        permission_classes=(IsAuthenticatedOrReadOnly, ),
        serializer_class=CoordinateSerializer,
    )
    def state(self, request, pk):
        station = get_object_or_404(Station, pk=pk)
        if request.method == 'GET':
            serializer = CoordinateSerializer(station)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = request.data
            instruction = Instructions.objects.create(
                user=request.user,
                axis=data['axis'],
                distance=data['distance']
            )
            axis_list = {
                'x': station.x,
                'y': station.y,
                'z': station.z
            }
            for axis in axis_list:
                if axis == instruction.axis:
                    coord = axis_list[axis] + instruction.distance
                    if coord < 0:
                        station.state = "broken"
                        station.date_broken = datetime.datetime.now(
                            tz=timezone.utc
                        )
                        station.save()
                    if axis == "x":
                        station.x = coord
                    elif axis == "y":
                        station.y = coord
                    else:
                        station.z = coord
            station.save()
            serializer = CoordinateSerializer(station)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
