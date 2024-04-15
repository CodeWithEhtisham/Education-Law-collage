
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', include('courses.course_admin.urls')),
    path('website/', include('courses.course_website.urls')),
]
