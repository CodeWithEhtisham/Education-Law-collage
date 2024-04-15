
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('website.home.urls')),
    path('about', include('website.about.urls')),
    path('contact', include('website.contact.urls')),
    path('admission', include('website.admission.urls')),
]
