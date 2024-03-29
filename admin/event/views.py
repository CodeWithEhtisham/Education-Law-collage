from django.shortcuts import render
from django.views import View
# Create your views here.

class CreateEventView(View):
    def get(self, request):
        return render(request, 'admin-event-add.html')
    

class EventListView(View):
    def get(self, request):
        return render(request, 'admin-event-all.html')