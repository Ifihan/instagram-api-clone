from accounts.models import AppUser
from django.db import models
from django.core.exceptions import SuspiciousOperation

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption
        # ___repr__

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    file = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.file.url

    @property
    def image_url(self):
        try:
            url = self.file.url
        except:
            url = None
        return url
 

# class BookmarkPost(models.Model):
#     user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user
