from django.shortcuts import render
from django.views import View
# Create your views here.
class CreateStudentView(View):
    def get(self, request):
        return render(request, 'admin-user-add.html')
    

class StudentListView(View):
    def get(self, request):
        return render(request, 'admin-user-all.html')