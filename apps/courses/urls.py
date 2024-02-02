from django.urls import path
from .views import CoursesView
urlpatterns = [
    path('courses',CoursesView.as_view(),name='courses'),
]
