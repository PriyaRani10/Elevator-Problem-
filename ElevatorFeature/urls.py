from django.urls import path

from .views import *

urlpatterns=[

    path('elevator-system/list/', ElevatorSystemList.as_view(), name='elevator-system-list'),
    path('elevator-system/<int:id>/list/',ElevatorsList.as_view(), name='elevator-list'),
]
