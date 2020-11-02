from django.db import models
from django.contrib.auth.models import User

# Profile class extends User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user_id: {self.user.id}'
