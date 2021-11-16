from posts.models import Posts
from rest_framework import serializers

from accounts.serializers import AppUserSerializer

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    user = AppUserSerializer(read_only=True)
    class Meta:
        model = Posts
        fields = ['id', 'user', 'caption', 'images', 'post_likes']