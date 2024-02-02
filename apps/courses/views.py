from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class CoursesView(TemplateView):
    template_name = 'courses.html'

    def get(self,requst):
        return render(requst,self.template_name)