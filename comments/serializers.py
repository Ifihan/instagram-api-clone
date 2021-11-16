from comments.models import Comments
from rest_framework import serializers
from posts.serializers import PostsSerializer

class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    post = PostsSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = ['id', 'post', 'comment']