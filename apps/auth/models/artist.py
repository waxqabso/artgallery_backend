from django.db import models
from django.contrib.auth.models import AbstractUser

class Artist(AbstractUser):
    class Meta:
        db_table = 'auth_user'
        name =  models.CharField(max_length = 50)
        email_address = models.CharField(max_length = 50)
        password = models.CharField(max_length = 255)
        phone_number = models.CharField(max_length = 50)
        address =  models.CharField(max_length = 50)
        biography = models.CharField(max_length = 255)
        profile_picture_path = models.ImageField()
        twitter = models.CharField(max_length = 50 )
        instagram = models.CharField(max_length = 50)
        facebook = models.CharField(max_length = 50)
        gender = models.BooleanField()
        rating =  models.DecimalField()
