
from django.contrib import admin
from django.urls import path,include
from backend_config.Swagger import schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('',include("mobile_api_user.urls")),
    path('account/',include('allauth.urls')),
    path('swagger/', schema_view.with_ui('swagger',
                cache_timeout=0), name='schema-swagger-ui'),

]
