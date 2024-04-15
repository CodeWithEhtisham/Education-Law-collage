from .views import *
from django.urls import path
urlpatterns = [
    path('list', AllCoursesView.as_view(), name='admin-all-courses'),
    path('create', CreateCourse.as_view(), name='admin-add-courses'),
]
