from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255)
    password2=serializers.CharField(max_length=255)

    def validate(self, data):
        username=data.get('username',None)
        password=data.get('password',None)
        password2=data.get('password2',None)
        if User.objects.filter(username=username):
            raise serializers.ValidationError({'username':'username da ton tai'})
        if password!=password2:
            raise serializers.ValidationError({'password':'password khong trung'})
        return data
    def create(self, validate_data):
        return User.objects.create(username=validate_data['username'], password=validate_data['password'])