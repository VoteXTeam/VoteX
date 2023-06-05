# sample rest serializer

from rest_framework import serializers
from VoteXApi.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'register_date', 'region', 'organization')


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name', 'register_date', 'region',
                  'organization', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def save(self, *args, **kwargs):
        region = self.validated_data['region']
        organization = self.validated_data['organization']
        custom_user = CustomUser(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            register_date=self.validated_data['register_date'],
            region=region,
            organization=organization,
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords Must Match'})
        custom_user.set_password(password)
        custom_user.save()
        return custom_user
