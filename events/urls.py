
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', include('events.event_admin.urls')),
    path('website/', include('events.event_website.urls')),
]
