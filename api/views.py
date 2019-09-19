from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pythinkutils.common.object2json import *
from pythinkutils.common.RetModel import RetModel

from rest_framework import generics, permissions, serializers
from django.contrib.auth.decorators import login_required

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, authentication

def hello(request):
    return HttpResponse(obj2json(RetModel()))
