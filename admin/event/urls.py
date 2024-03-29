from django.urls import path
from .views import *

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('create/', CreateEventView.as_view(), name='event-create'),
]