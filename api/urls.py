from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^hello$', views.hello, name='hello'),
]