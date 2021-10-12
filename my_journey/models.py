from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    image_url = models.TextField()
    likes = models.BigIntegerField()
    dislikes = models.BigIntegerField()
    comments = ArrayField(models.TextField())

    def __str__(self):
        return self.image_url
