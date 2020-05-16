from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from authentication.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserLoginSerializer,RegistrationSerializer,HospitalRegistrationSerializer,ClinicRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from authentication.models import CustomUser
from django.contrib.auth.models import update_last_login
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER        

def get_token(user):
    try:
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        update_last_login(None, user)
    except CustomUser.DoesNotExist:
        return  'User with given email and password does not exists'
            
    return {
             jwt_token
        }

#view for creating user login info
class UserRegistrationView(CreateAPIView):
    parser_classes=[JSONParser,]
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        email=request.data.get("email",None)
        password=request.data.get("password",None)
        user=authenticate(email=email,password=password)
        token=get_token(user)
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            'token':token,
            }
        
        return Response(response, status=status_code)
#view for creating hospital data
class HospitalRegistration(CreateAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    parser_classes=[JSONParser,]
    serializer_class = HospitalRegistrationSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'hospital registered  successfully',
        }
        return Response(response,status=status_code)

#view for creating clinic info

class ClinicRegistration(CreateAPIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(JSONWebTokenAuthentication,)
    parser_classes=[JSONParser,]
    serializer_class = ClinicRegistrationSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'clinic registered  successfully',
        }
        return Response(response,status=status_code)

#view for login 
class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
