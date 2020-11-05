from django.db import models
from django.contrib.auth.models import User
from .City import City
from .Profile import Profile

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title}, author: {self.author}'

