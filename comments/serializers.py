from posts.serializers import PostsSerializer
from rest_framework import serializers

from .models import Comment


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    post = PostsSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "comment"]
