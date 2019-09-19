from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pythinkutils.common.object2json import *
from pythinkutils.common.RetModel import RetModel
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

from django.urls import URLPattern, URLResolver

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def hello(request):
    return HttpResponse(obj2json(RetModel()))

class ApiFxxk(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(obj2json(RetModel(data="Hello, OAuth2!")))

# @method_decorator(csrf_exempt)
class ApiFxxkPlus(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(obj2json(RetModel(data="GET FXXK, OAuth2!")))

    # @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        return HttpResponse(obj2json(RetModel(data="POST FXXK, OAuth2!")))
