from django.conf.urls import url
from api import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^hello$', views.hello, name='hello'),
    url(r'^fxxk$', views.ApiFxxk.as_view()),  # an example resource endpoint
    url(r'^fxxk-plus/*', csrf_exempt(views.ApiFxxkPlus.as_view())),  # an example resource endpoint
]