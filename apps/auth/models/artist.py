from django.db import models
from django.contrib.auth.models import AbstractUser

class Artist(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    pass
