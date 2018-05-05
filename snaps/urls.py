from django.conf.urls import url 
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.index, name='index'),
    url(r'^search/', views.search_photos, name='searchPhotos'),
    url(r'^location/', views.filter_location, name='locationPhoto')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)