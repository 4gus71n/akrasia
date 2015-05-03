from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html'), name="Home"),
    url(r'^api/', include('akrasia_messages.urls'))
]

