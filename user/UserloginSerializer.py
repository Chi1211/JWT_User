from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255, write_only=True)
    token=serializers.CharField(max_length=255, read_only=True)
    
    def validate(self,data):
        username=data.get('username',None)
        password=data.get('password', None)
        user=authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
            'tài khoản k tồn tại'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
        'User with given email and password does not exists')
        else:
            data['user']= user
            data['token']=jwt_token
            

            return data