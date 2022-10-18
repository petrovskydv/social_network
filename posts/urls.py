from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from posts.views import UserSingUp, PostCreate

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('singup/', UserSingUp.as_view(), name='singup'),
    path('post/', PostCreate.as_view(), name='post'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
