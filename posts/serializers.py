from posts.models import Post, Image
from rest_framework import serializers

from accounts.models import AppUser
from accounts.serializers import AppUserSerializer

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = ['image_url']

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    user = AppUserSerializer(read_only=True)
    post_images = ImageSerializer(many=True, read_only=True, source="images")

    def create(self, validated_data):
        image_data = self.context.get("request").FILES.getlist("file")
        current_user = AppUser.objects.first()
        validated_data.update({"user_id": current_user.id})
        post = Post.objects.create(**validated_data)
        for image in image_data:
            Image.objects.create(post=post, file=image)

        print(post.images)
        return post

    class Meta:
        model = Post
        fields = ['id', 'user', 'caption', "post_images"]
