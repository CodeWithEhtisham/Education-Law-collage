from django.urls import path
from .views import *
urlpatterns = [
    path("", StudentListView.as_view(), name="student-list"),
    path("create/", CreateStudentView.as_view(), name="student-create"),
]