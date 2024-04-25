from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializr(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Username is already Taken')
        return data