from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^perfil$', TemplateView.as_view(template_name="backend/perfil.html"), 
        name='perfil'),
]