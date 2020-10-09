from rest_framework import serializers
from .models import Player, User

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'name',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('accessId', 'nickname', 'level',)
