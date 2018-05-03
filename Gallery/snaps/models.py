from django.db import models

# Create your models here.
class Photo(models.Model):
    Image_name= models.CharField(max_length=30)
    Image_description=models.CharField(max_length=200)
    Image_url=models.ImageField(upload_to='articles/')
    source=models.CharField(max_length=20)

    def __str__(self):
        return self.Image_name

    def save_photo(self):
        self.save()
    @classmethod
    def display_photos(self):
        photos= Photo.objects.all()
        print(photos)
        return photos



