from django.conf.urls import url
from akrasia_messages import views

urlpatterns = [
    url(r'^messages/$', views.message_list),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.message_detail),
]