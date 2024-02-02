from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class StudentsView(TemplateView):
    template_name = 'students.html'

    def get(self,request):
        return render(request,self.template_name)