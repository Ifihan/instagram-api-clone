from django.db import models
from accounts.models import AppUser

# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Posts(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.caption

class BookmarkPost(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user