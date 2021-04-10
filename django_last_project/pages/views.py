from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = '<h1>Hello World</h1>'
    return HttpResponse(html)
