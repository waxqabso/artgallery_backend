from django.db import models

from utils.models import Timestamped

# Create your models here.

MEDIA_UPLOAD_PATH = './media'
ART_UPLOAD_PATH = MEDIA_UPLOAD_PATH+'/art'

class Art(Timestamped):

    class Availability:
        AVAILABLE_NOW = 'AN'
        AVAILABLE_LATER = 'AL'
        NOT_AVAILABLE = 'NA'
        CHOICES = {
            (AVAILABLE_NOW, 'Available Now'),
            (AVAILABLE_LATER, 'Available for Order'),
            (NOT_AVAILABLE, 'Not Available'),
        }

    availability = models.CharField(
        max_length=2,
        choices=Availability.CHOICES,
        default=Availability.AVAILABLE_NOW,
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=ART_UPLOAD_PATH, blank=True)
    rating = models.IntegerField(default=0)
    #artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    timeframe_for_order = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=15)
