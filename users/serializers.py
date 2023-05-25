from rest_framework import serializers
from users.models import RegisteredUsers
from rest_framework.validators import UniqueValidator


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField()

    class Meta:
        model = RegisteredUsers
        fields = ['token']


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=4, validators=[UniqueValidator(queryset=RegisteredUsers.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=RegisteredUsers.objects.all())])

    class Meta:
        model = RegisteredUsers
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}
