from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializr(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username').lower()
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username is already taken')
        return data
    def create(self, validated_data):
        user = User.objects.create(first_name = validated_data['first_name'],
                                   last_name = validated_data['last_name'],
                                   username = validated_data['username'].lower())
        user.set_password(validated_data['password'])
        return user