from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="backend/perfil.html"), 
        name='perfil'),
]