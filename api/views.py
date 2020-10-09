from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Player
from .serializers import (
    PlayerSerializer,
)

# Create your views here.
@api_view(['GET'])
def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    serializer = PlayerSerializer(player)
    return Response(serializer.data)

