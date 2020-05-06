from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# defining a view as a function. 
# a python object representing an http request
def myView(request):
    return HttpResponse('Hello, World!') 