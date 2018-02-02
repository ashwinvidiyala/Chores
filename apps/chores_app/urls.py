from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_child$', views.add_child),
    url(r'^$', views.index),
    url(r'^index$', views.index),
]
