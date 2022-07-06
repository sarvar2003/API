from rest_framework import generics
from users.serializers import AuthTokenSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class AuthTokenView(ObtainAuthToken):
    """Create a new token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    