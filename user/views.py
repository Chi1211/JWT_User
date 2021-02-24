from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .UserloginSerializer import UserLoginSerializer
from .RegisterSerializer import RegisterSerializer
from django.contrib.auth import login
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
# Create your views here.
class UserloginView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'home.html'
    permission_classes = (AllowAny,)
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):

        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # token, created = Token.objects.get_or_create(user=user)
        login(request, user)       
        response = {
        
        'username': user.username,
        'password': user.password,
        'status_code' : status.HTTP_200_OK,
        'token': serializer.validated_data['token'],
        }
        status_code = status.HTTP_200_OK
        
        return Response(response, status=status_code)

class UserRegister(APIView):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Register successful!',
                'status_code' : status.HTTP_200_OK,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else: return Response({'message': 'Register errors!', }, status=400)
        



