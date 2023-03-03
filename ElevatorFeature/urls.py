from django.urls import path

from .views import *

urlpatterns=[

    path('elevator-system/list/', ElevatorSystemList.as_view(), name='elevator-system-list'),
    path('elevator-system/<int:id>/list/',ElevatorsList.as_view(), name='elevator-list'),
   
    path('elevator-system/add-new/', CreateElevatorSystem.as_view(),name='add-new-elevator-system'),
    #  url for each requesting elevator view and update 
    path('elevator-system/<int:id>/elevator/<int:pk>/detail/', ViewUpdateSingleElevatorDetail.as_view(),name='each-elevator-detail-view-and-update'),
    # url for view and add new req
    path('elevator-system/<int:id>/elevator/<int:pk>/add-new-req/', ListCreateElevatorRequest.as_view(),name='add-new-request-and view'),


]
