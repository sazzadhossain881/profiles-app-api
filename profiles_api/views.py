from django.shortcuts import render
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

class UserLoginViewSet(ObtainAuthToken):
    """handle create user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileFeedItemSerializer
    queryset = models.UserProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnFeed,
        IsAuthenticated,
        )

    def perform_create(self, serializer):
        """set the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
