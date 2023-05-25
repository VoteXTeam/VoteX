# sample rest serializer

from rest_framework import serializers
from VoteXApi.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
