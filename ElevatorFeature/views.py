from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ElevatorSystem, Elevator, ElevatorRequest
from .serializers import ElevatorSystemSerializer, ElevatorSerializer, ElevatorRequestSerializer,ElevatorRequestSerializerAll


class ElevatorSystemList(generics.ListAPIView):
  '''
  get all elevator systems.
  '''
  queryset = ElevatorSystem.objects.all()
  serializer_class = ElevatorSystemSerializer



class ElevatorsList(generics.ListAPIView):
  '''
  Given an elevator system, listing out all the elevators and their status. 
  '''
  serializer_class = ElevatorSerializer

  def get_queryset(self):
    system_id = self.kwargs['id']
    queryset = Elevator.objects.filter(elevator_system__id = system_id)

    return queryset


