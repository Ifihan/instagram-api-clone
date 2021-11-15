from posts.models import Posts
from rest_framework import serializers

from accounts.serializers import AppUserSerializer

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    author = AppUserSerializer(read_only=True)
    class Meta:
        model = Posts
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at')
