from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class EventsView(TemplateView):
    template_name = 'events.html'

    def get(self,request):
        return render(request,self.template_name)