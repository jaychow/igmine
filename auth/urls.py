from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hubchallenge/$', views.hubchallenge, name="hubchallenge"),
]