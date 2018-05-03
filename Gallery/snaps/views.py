from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Category, Location
# Create your views here.

def index(request):
    title="Snaps | Home"
    photos= Photo.display_photos()
    return render(request, 
    'gallery/index.html', {"title": title, "photos":photos})

def search_photos(request):
    if 'category' in request.GET and request.GET["category"]:
        searched_photos = request.GET.get('category')
        searched_category= Photo.search_photo(search_photos)
        message= f'{searched_photos}'
        print(searched_category)
        title="Snaps | search"
        return render(request,'gallery/search.html', {"title":title, "message": message, "category":searched_category})
    else:
        title="Snaps | search "
        message="You haven't searched for any term"
        return render(request, 'gallery/search.html', {"message":message,"title":title})