from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, name):
    return HttpResponse('<h1>Hello {}</h1>'.format(name))

