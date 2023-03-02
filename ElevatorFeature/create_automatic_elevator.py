from .models import Elevator

def create_elevators(number_of_elevators : int,system_id : int):
  '''
  here, it will automatically create elevators inside an elevator system
  Given the system id and number of elevators. This function will run, once
  the elevator is created
  '''

  for i in range(number_of_elevators):
    elevator_object = Elevator.objects.create(
      elevator_system_id = system_id,
      elevator_number = i+1,
    )

    elevator_object.save()