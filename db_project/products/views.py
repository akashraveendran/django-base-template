from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def sample(request):
    return HttpResponse("Hello world!")

def view_sample_page(request):
    return render(request,"sample.html")