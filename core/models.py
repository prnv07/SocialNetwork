from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    follows = models.ManyToManyField("self", related_name="followers", symmetrical=False)
    #profile_pic=models.ImageField()

    def __str__(self):
        return self.user


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField
    likes = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField
    published_date = models.DateTimeField(auto_now_add=True)

