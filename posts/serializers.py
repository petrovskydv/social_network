from rest_framework import serializers

from posts.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializes User model"""

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'], name=validated_data['name'], password=validated_data['password']
        )
        return user
