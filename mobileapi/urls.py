

from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',home,name='home'),
    path('user/create',UserRegistrationView.as_view(), name='create_mobile_user'),
    path('user/login',update_user_data.as_view()),
    path('user/loginjwt', Loginapi_views_jwt.as_view()),
    path('home', Home.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
