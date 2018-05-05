from django.db import models
import pyperclip

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)

    def save_category(self):
        self.save()
    @classmethod
    def display_categories(cls):
        categories=Category.objects.all()
        return categories



    def __str__(self):
        return self.name

class Location(models.Model):
    name= models.CharField(max_length=100)

    def save_location(self):
        self.save()

    @classmethod
    def display_locations(cls):
        locations=cls.objects.all()
        return locations
    
        
    

    


    def __str__(self):
        return self.name

class Photo(models.Model):
    title= models.CharField(max_length=30)
    Image_description=models.CharField(max_length=200)
    Image_url=models.ImageField(upload_to='articles/')
    source=models.CharField(max_length=20)
    image_category=models.ForeignKey(Category)
    image_location=models.ForeignKey(Location)



    def __str__(self):
        return self.title



    def save_photo(self):
        self.save()

    def find_image(self):
        return self.objects.get(pk=id)
    @classmethod
    def display_photos(self):
        photos= Photo.objects.all()
        return photos

    @classmethod
    def search_photo(cls, search_photos):
        found_photo= cls.objects.filter(image_category__name__icontains=search_photos)
        return found_photo

    @classmethod
    def save_url(self):
        url= self.objects.add(Image_url="hello")
        copy=pyperclip.copy(url)
        print(copy)
        return copy
   
    @classmethod
    def image_bylocation(cls, image_location):
       location=cls.objects.filter(image_location__name=image_location)
       return location
    







