from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Category, Location
# Create your views here.

def index(request):
    title="Snaps | Home"
    photos= Photo.display_photos()
    categories=Category.display_categories()
    return render(request, 
    'gallery/index.html', {"title": title, "photos":photos, "categories":categories})

def search_photos(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get('category')
        searched_category = Photo.search_photo(search_term)
        message= f'{search_term}'
        print(searched_category)
        title="Snaps | search"
        return render(request,'gallery/search.html', {"title":title, "message": message, "category":searched_category})
    else:
        title="Snaps | search "
        message="You haven't searched for any term"
        return render(request, 'gallery/search.html', {"message":message,"title":title})
