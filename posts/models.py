from django.db import models
from accounts.models import AppUser

# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption