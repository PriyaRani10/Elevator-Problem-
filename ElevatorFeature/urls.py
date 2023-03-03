from django.urls import path

from .views import *

urlpatterns=[

    # url for post and get the single elevator
    path('elevator-system/list/', ElevatorSystemList.as_view(), name='elevator-system-list'),
    path('elevator-system/<int:id>/list/',ElevatorsList.as_view(), name='elevator-list'),
   
   # url for create  whole new elevator system
    path('elevator-system/add-new/', CreateElevatorSystem.as_view(),name='add-new-elevator-system'),
    
    #  url for each requesting elevator view and update 
    path('elevator-system/<int:id>/elevator/<int:pk>/detail/', ViewUpdateSingleElevatorDetail.as_view(),name='each-elevator-detail-view-and-update'),
    
    # url for view and add new req
    path('elevator-system/<int:id>/elevator/<int:pk>/add-new-req/', ListCreateElevatorRequest.as_view(),name='add-new-request-and view'),

    # to fetch the destination
    path('elevator-system/<int:id>/elevator/<int:pk>/destination/',FetchDestinationView.as_view(),name='fetch-destination'),

]
