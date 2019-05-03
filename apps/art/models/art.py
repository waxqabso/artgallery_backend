from django.db import models

# Create your models here.

class Art(models.Model):

    class Availability:
        AVAILABLE_NOW = 'AN'
        AVAILABLE_LATER = 'AL'
        NOT_AVAILABLE = 'NA'
        CHOICES = {
            (AVAILABLE_NOW = 'Available Now')
            (AVAILABLE_LATER = 'Available for Order')
            (NOT_AVAILABLE = 'Not Available')
        }

    availability = models.CharField(
        max_length=2,
        choices=Availability.CHOICES,
        default=AVAILABLE_NOW,
    )

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_new_add=True)
    image = models.ImageField()
    rating = models.IntegerField(default=0)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    timeframe_for_order = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2)
