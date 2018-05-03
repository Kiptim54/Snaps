from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    title="Snaps | Home"
    return render(request, 'gallery/index.html', {"title": title})
