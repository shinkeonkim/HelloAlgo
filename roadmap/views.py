from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def showRoadmap(request):
    return render(request, 'showRoadmap.html')