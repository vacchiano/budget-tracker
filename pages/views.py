from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    #check if the user is logged in - if so, redirect to dashboard
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard'))
        return super(HomePageView, self).get(request, *args, **kwargs)


class AboutPageView(TemplateView):
    template_name = 'about.html'