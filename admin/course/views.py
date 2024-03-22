from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class AllCoursesView(TemplateView):
    template_name = 'admin-all-courses.html'

    def get(self,request):
        return render(request,self.template_name)
    

class CreateCourse(TemplateView):
    template_name = 'admin-add-courses.html'

    def get(self,request):
        return render(request,self.template_name) 