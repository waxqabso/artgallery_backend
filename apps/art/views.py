from art.models import Art
from rest_framework import viewsets
from art.serializers import ArtSerializer


class ArtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Art.objects.all().order_by('-created_at')
    serializer_class = ArtSerializer
