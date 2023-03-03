from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

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


class ViewUpdateSingleElevatorDetail(generics.RetrieveUpdateAPIView):
  '''
  Getting the details of a specific elevator that we want, 
  given its elevator system and elevator number.
  Also,
  Update details of a specific elevator, 
  given its elevator system and elevator number in URL
  '''
  serializer_class = ElevatorSerializer

  def  get_object(self):
    system_id = self.kwargs['id']
    elevator_number = self.kwargs['pk']

    queryset = Elevator.objects.filter(
      elevator_system__id = system_id,
      elevator_number = elevator_number
    )

    return queryset[0]
  
  #override this  put method by patch for partial update
  def put(self, request, *args, **kwargs):
    return self.partial_update(request, *args, **kwargs)
  

class ListCreateElevatorRequest(generics.ListCreateAPIView):
  '''
  Create a new request for a specific elevator, 
  given its elevator system and elevator number in URL.
  The inputs of requested and destinatiom floor is sent with
  the form-data.
  '''
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['is_active']
  
  def get_serializer_class(self, *args, **kwargs):
    return ElevatorRequestSerializer if self.request.method == 'POST' else ElevatorRequestSerializerAll
      
  # Overriding the perform_create method, Parent class of 'CreateAPIView'
  def perform_create(self, serializer):
    system_id = self.kwargs['id']
    elevator_number = self.kwargs['pk']

    elevator_object = Elevator.objects.get(
      elevator_system__id = system_id,
      elevator_number = elevator_number
    )
    # elevator_object = queryset[0]

    serializer.save(elevator = elevator_object)


  '''
  List all the requests for a given elevator
  Requests already served can be filtered with is_active
  parameter set false
  '''
  def get_queryset(self):
    system_id = self.kwargs['id']
    elevator_number = self.kwargs['pk']

    elevator_object = Elevator.objects.get(
      elevator_system__id = system_id,
      elevator_number = elevator_number
    )

    queryset = ElevatorRequest.objects.filter(elevator = elevator_object)
    return queryset
    


  


