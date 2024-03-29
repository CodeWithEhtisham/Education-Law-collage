from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class SiteSettingView(TemplateView):
    template_name = 'admin-setting.html'

    def get(self,request):
        return render(request,self.template_name)