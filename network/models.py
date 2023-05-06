from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    following = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True)

    def number_of_following(self):
        return self.following.count()

    def number_of_followers(self):
        return self.followers.count()

    def __str__(self):
        return f"{self.username}"
    


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    content = models.CharField(max_length=128)
    timestamp = models.CharField(max_length=64, default="bro", blank=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    time = models.DateTimeField(default=datetime.today())

    def number_of_likes(self):
        return self.likes.count()
    

    


    

