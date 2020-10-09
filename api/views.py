from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Player, User
from .serializers import (
    PlayerSerializer,
    UserSerializer,
)

# Create your views here.
@api_view(['GET'])
def player(request, name):
    player = Player.objects.filter(name=name)
    serializer = PlayerSerializer(player, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user(request, nickname):
    user = get_object_or_404(User, nickname=nickname)
    serializer = UserSerializer(user)
    return Response(serializer.data)
