from django.conf.urls import url
from django.views.generic import TemplateView

from landing.views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="landing/index.html"), 
        name='index'),
    url(r'^$', TemplateView.as_view(template_name="landing/login.html"), 
        name='login'),
    url(r'^$', TemplateView.as_view(template_name="landing/register.html"), 
        name='register'),
]