from django.db import models
from django.contrib.auth.models import User
from .City import City


# Profile class extends User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    email = models.CharField(max_length=200, default='', blank=True)
    img_url = models.CharField(max_length=500, default='', blank=True)
    bio = models.TextField(max_length=1000, default='', blank=True)

    def __str__(self):
        return f'user_id: {self.user.id}'

    # def get_dict()
