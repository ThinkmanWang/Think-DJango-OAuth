from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^hello$', views.hello, name='hello'),
    url(r'^fxxk$', views.ApiFxxk.as_view()),  # an example resource endpoint
    url(r'^fxxk-plus/*', views.ApiFxxkPlus.as_view()),  # an example resource endpoint
]