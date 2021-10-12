from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=200, null=False)
    friends = ArrayField(models.TextField(), blank=True)

    def __str__(self):
        return self.username

class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    image_url = models.TextField(null=False)
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)
    comments = ArrayField(models.TextField(), blank=True)

    def __str__(self):
        return self.image_url