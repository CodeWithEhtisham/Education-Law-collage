from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self,request):
        return render(request,self.template_name)