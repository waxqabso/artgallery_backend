from django.db import models

class Timestamped(models.Model):
    """Abstract class that is used to provide a way to keep track of when the model is created and updated"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True