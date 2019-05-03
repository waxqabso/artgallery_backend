from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


MEDIA_UPLOAD_PATH = './media/artist'

class Artist(models.Model):

    name =  models.CharField(max_length = 50)
    email_address = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 255)
    phone_number = PhoneNumberField()
    address =  models.TextField(max_length = 50 , blank = True)
    biography = models.TextField(blank = True)
    profile_picture_path = models.ImageField(upload_to=MEDIA_UPLOAD_PATH)
    twitter = models.URLField(max_length = 50 , blank = True)
    instagram = models.URLField(max_length = 50, blank = True)
    facebook = models.URLField(max_length = 50, blank = True)
    gender = models.BooleanField()
    rating =  models.IntegerField()

