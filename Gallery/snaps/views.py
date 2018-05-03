from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
# Create your views here.

def index(request):
    title="Snaps | Home"
    photos= Photo.display_photos()
    return render(request, 
    'gallery/index.html', {"title": title, "photos":photos})
