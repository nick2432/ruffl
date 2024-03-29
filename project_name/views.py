from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
    return render(request, 'index.html')

def serve_static(request, path):
    file_path = os.path.join(settings.STATIC_ROOT, path)
    return HttpResponse(open(file_path, 'rb'), content_type='text/html')
