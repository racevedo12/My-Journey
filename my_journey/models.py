from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.TextField(null=False)
    likes = models.ManyToManyField(User, related_name="user_picture_likes")
    dislikes = models.ManyToManyField(User, related_name="user_picture_dislikes")

    def __str__(self):
        return self.image_url

    # Defining an absolute url for the model in order to redirect the page after a post request
    def get_absolute_url(self):
        return reverse("user_home_page")

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

class Comment(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name="picture_comments")
    text = models.TextField(null=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.text