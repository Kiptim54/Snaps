from django.test import TestCase
from .models import Photo

# Create your tests here.

class PhotoTestClass(TestCase):
    #setting up
    def setUp(self):
        self.new_photo= Photo(Image_name="The sun", Image_description="The sun in its glory", Image_url="#", source="Brenda Kiptim")

        #Test the instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_photo, Photo))

    def test_savephoto(self):
        self.new_photo.save_photo()
        photos= Photo.objects.all()
        self.assertTrue(len(photos)>0)

    # def test_deletephoto(self):
        
    def tearDown(self):
        Photo.objects.all().delete()
    

    
