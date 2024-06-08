from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics, status 
from .models import User_mobile,Service
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .Serializer import LoginAPIView ,User_mobile_serialize,ServiceSerializer
from rest_framework_simplejwt.tokens import RefreshToken 
from .jwt_token import *


def home(request):
    print("asdasd",request.user)
    return render(request, 'home.html')


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = User_mobile_serialize
    queryset = User_mobile.objects.all()

    
class update_user_data(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, number):
        try:
            print(User_mobile.objects.all())
            print(number)           
            return User_mobile.objects.get(mobile_number=number)
        except User_mobile.DoesNotExist:
            raise Http404("user not  exist ")

    def put(self,request, format=None):
        data_item=request.data
        print(data_item)
        number=data_item.get('phone_number',None)
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
    




class User_book_apointment(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        pass

class UserMobileListAPIView(generics.ListAPIView):
    queryset = User_mobile.objects.all()
    # serializer_class = UserMobileSerializer

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            # accessToken = request.data["access_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"Referse token is deleted "}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"you already deleted this token"}, status=status.HTTP_200_OK)


class fetch_all_Service(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        return Service.objects.all()


