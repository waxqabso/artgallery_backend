from art.models import Art
from rest_framework import serializers


class ArtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Art
        fields = ('name', 'description', 'created', 'rating', 'image','timeframe_for_order', 'price')
