from rest_framework.generics import CreateAPIView

from posts.models import User
from posts.serializers import UserSerializer


class UserSingUp(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
