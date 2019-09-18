from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pythinkutils.common.object2json import *
from pythinkutils.common.RetModel import RetModel

def hello(request):
    return HttpResponse(obj2json(RetModel()))