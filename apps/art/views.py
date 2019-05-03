from art.models import Art
from art.models import Artist
from rest_framework import viewsets
from art.serializers import ArtSerializer
from art.serializers import ArtistSerializer


class ArtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Art.objects.all().order_by('-created')
    serializer_class = ArtSerializer

class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
