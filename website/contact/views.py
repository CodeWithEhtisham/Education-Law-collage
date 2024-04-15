from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ContactUsView(TemplateView):
    template_name = 'contact-us.html'

    def get(self,request):
        return render(request,self.template_name)