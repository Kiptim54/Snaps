from django.test import TestCase
from .models import Photo, Category, Location

# Create your tests here.
class CategoryTest(TestCase):
    def setUp(self):
        self.new_category=Category(name="Food")


    def test_savecategory(self):
        self.new_category.save_category()
        photos= Category.objects.all()
        self.assertTrue(len(photos)>0)
    
    
class PhotoTestClass(TestCase):
    #setting up
    def setUp(self):
        
        self.new_photo= Photo(title="The sun", Image_description="The sun in its glory", Image_url="jjj.jpeg", source="Brenda Kiptim", image_location=Location(id), image_category=Category(id))
        
        #Test the instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_photo, Photo))

    def test_savephoto(self):
        self.new_photo.save_photo()
        photos= Photo.objects.all()
        self.assertTrue(len(photos)>0)

    # def test_deletephoto(self):
        
    # def tearDown(self):
    #     Photo.objects.all().delete()
    

    
