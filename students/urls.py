
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', include('students.student_admin.urls')),
    path('dashboard/', include('students.student_dashboard.urls')),
]
