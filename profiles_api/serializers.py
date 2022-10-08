from rest_framework import serializers
from profiles_api import models



class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],

        )
        return user
class UserProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializes profile feed item"""
    class Meta:
        model = models.UserProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'create_on')
        extra_kwargs = {
            'user_profile':{
                'read_only':True,
            }
        }
