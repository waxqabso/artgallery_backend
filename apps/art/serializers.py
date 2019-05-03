from art.models import Art
from art.models import Artist
from rest_framework import serializers


class ArtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Art
<<<<<<< HEAD
        fields = ('name', 'description', 'created', 'rating', 'image','timeframe_for_order', 'price', 'availability')
=======
        fields = ('name', 'description', 'created', 'rating', 'image','timeframe_for_order', 'price', 'availability')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'email_address', 'password', 'phone_number', 'address', 'biography',
        'profile_picture_path', 'twitter', 'instagram', 'facebook', 'gender', 'rating')
>>>>>>> Artist CRUD operations
