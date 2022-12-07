from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def world(request):
    return HttpResponse("<p>My first request</p>")