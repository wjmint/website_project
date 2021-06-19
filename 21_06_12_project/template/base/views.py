from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def others(request):
    return render(request, 'base/others.html')

def relatives(request):
    return render(request, 'base/relatives.html')