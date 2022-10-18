from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from posts.views import UserSingUpView, PostCreateView, LikeView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('singup/', UserSingUpView.as_view(), name='singup'),
    path('post/', PostCreateView.as_view(), name='post'),
    path('post/<int:pk>/like', LikeView.as_view(), name='like'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
