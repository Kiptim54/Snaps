from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Category, Location
# Create your views here.

def index(request):
    title="Snaps | Home"
    photos= Photo.display_photos()
    locations=Location.display_locations()
    return render(request, 
    'gallery/index.html', {"title": title, "photos":photos, "locations":locations})

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

    
def search_location(request):
    if 'location' in request.GET and request.GET["location"]:
        search_locs = request.GET.get('location')
        searched_location = Photo.search_location(search_locs)
        message= f'{search_locs}'
        print(searched_location)
        title="Snaps | search"
        return render(request,'gallery/location.html', {"title":title, "message": message, "location":searched_location})
    else:
        title="Snaps | search "
        message="You haven't searched for any term"
        return render(request, 'gallery/location.html', {"message":message,"title":title})




    
