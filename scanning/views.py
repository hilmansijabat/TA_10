from django.shortcuts import render
from django.conf import settings
import os


# Create your views here.

# TODO: Create view for index
def index(request):
    context = {}
    return render(request, 'scanning/index.html', context)

def scanning_request(request):
    context = {}
    return render(request, 'scanning/scanning.html', context)

# def detail(request):
#     context = {}
#     return render(request, 'scanning/detail.html', context)