from django.shortcuts import render
from rest_framework import generics, status
from .Serializers import User_mobile_serialize
from .models import User_mobile
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .Serializers import LoginAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .jwt_token import *


def home(request):
    print(request.user)
    return render(request, 'home.html')


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = User_mobile_serialize
    queryset = User_mobile.objects.all()

    
class update_user_data(APIView):
    
    def get_object(self, number):
        try:            
            return User_mobile.objects.get(mobile_number=number)
        except User_mobile.DoesNotExist:
            raise Http404("user not  exist ")
        
    def log_view_data(self,**data):
        try:
            phone_number=data.get('phonenumber')
            password_login=data.get('password')
            data=User_mobile.objects.get(mobile_number=phone_number,password=password_login)
            return data
        except:
            raise Http404("userphone_number is not register")
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self,request,format=None):
        pass
    
    def put(self,request, format=None):
        data_item=request.data
        number=data_item.get('phonenumber',None)
        data_obj = self.get_object(number)

        serializer = User_mobile_serialize(data_obj, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User data is updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Loginapi_views_jwt(APIView):
    serializer_class = LoginAPIView

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['phonenumber']
            password = serializer.validated_data['password']
            user_stat = User_mobile.objects.filter(mobile_number=user_name).first()
            if user_stat and user_stat.check_password(password):

                refresh = CustomRefreshToken.for_user(user_stat)
                access = CustomAccessToken.for_user(user_stat)
                data = {
                    'refresh': str(refresh),
                    'access': str(access),
                    'user': User_mobile_serialize(user_stat).data
                }

                return Response({'message': data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        return Response({"message":User_mobile_serialize(request.user).data}, status=status.HTTP_200_OK)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=204)
        except Exception as e:
            return Response(status=400)




