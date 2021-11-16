from django.db import models
from posts.models import Posts

# Create your models here.
class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)