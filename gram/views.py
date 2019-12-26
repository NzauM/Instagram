from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404



# Create your views here.

def timeline(request):
    return render(request,'timeline.html')
    