from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.TextField(null=False)
    likes = models.ManyToManyField(User, related_name="user_picture")
    dislikes = models.BigIntegerField(default=0)
    comments = ArrayField(models.TextField(), blank=True, null=True)

    def __str__(self):
        return self.image_url

    # Defining an absolute url for the model in order to redirect the page after a post request
    def get_absolute_url(self):
        return reverse("user_home_page")

    def total_likes(self):
        return self.likes.count()