from posts.models import Posts, Images
from rest_framework import serializers

from accounts.models import AppUser
from accounts.serializers import AppUserSerializer

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    user = AppUserSerializer(read_only=True)

    def create(self, validated_data):
        image_data = self.context.get("request").FILES.get("attachment")
        current_user = AppUser.objects.first()
        validated_data.update({"user_id": current_user.id})

        

    class Meta:
        model = Posts
        fields = ['id', 'user', 'caption', 'images', 'post_likes']