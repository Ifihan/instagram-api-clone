from posts.serializers import PostsSerializer
from rest_framework import serializers

from .models import Comments


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    post = PostsSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ["id", "post", "comment"]
