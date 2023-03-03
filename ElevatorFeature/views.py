from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ElevatorSystem, Elevator, ElevatorRequest
from .serializers import ElevatorSystemSerializer, ElevatorSerializer, ElevatorRequestSerializer,ElevatorRequestSerializerAll

from .create_automatic_elevator import create_elevators

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


class CreateElevatorSystem(generics.CreateAPIView):
  '''
  Create a new elevator system.
  '''
  serializer_class = ElevatorSystemSerializer

  def perform_create(self, serializer):
    serializer.save()

    # Created elevators needed for the system. so, imported create_automatic_elevators.py
    create_elevators(
      number_of_elevators=serializer.data['number_of_elevators'],
      system_id=serializer.data['id']
    )
  
  


