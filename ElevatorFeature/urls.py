from django.urls import path

from .views import *

urlpatterns=[

    path('elevator-system/list/', ElevatorSystemList.as_view(), name='elevator-system-list'),
    path('elevator-system/<int:id>/list/',ElevatorsList.as_view(), name='elevator-list'),
   
    path('elevator-system/add-new/', CreateElevatorSystem.as_view(),name='add-new-elevator-system'),

    path('elevator-system/<int:id>/elevator/<int:pk>/detail/', ViewSingleElevatorDetail.as_view(),name='each-elevator-detail-view'),

]
