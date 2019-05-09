from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def evaluate(request):
    return HttpResponse("<html><title>PAF</title></html>")
