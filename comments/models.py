from django.db import models
from accounts.models import AppUser

# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment