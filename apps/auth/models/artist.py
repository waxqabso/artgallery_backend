from django.db import models
from django.contrib.auth.models import AbstractUser

class Artist(AbstractUser):

      name =  models.CharField(max_length = 50)
      email_address = models.EmailField(max_length = 254)
      password = models.CharField(max_length = 255)
      phone_number = models.PhoneNumberField()
      address =  models.TextField(max_length = 50 , blank = True)
      biography = models.TextField(blank = True)
      profile_picture_path = models.ImageField()
      twitter = models.URLField(max_length = 50 , blank = True)
      instagram = models.URLField(max_length = 50, blank = True)
      facebook = models.URLField(max_length = 50, blank = True)
      gender = models.BooleanField()
      rating =  models.IntegerField()

    class Meta:
        db_table = 'auth_user'
